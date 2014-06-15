from __future__ import division
import ctypes
import pickle
import os
import time
import logging
import SHAPI
from pylab import *

CAL_FILE_NAME = 'SHCAL.bin'

FS = 486111.1
DEFAULT_CONFIG = {'attenVal':10, 'mixerBand':1, 'sensitivity':0,
                  'decimation':1,'IF_Path':0, 'ADC_clock':0}

MIXER_BANDS = {'low':0, 'high':1}
MIXER_LOW_BAND_EDGE = 150e6

POWER_BANDWIDTH = 200e3

IF_PATHS = {10.7:0, 2.9:1}
ADC_CLOCKS = {23.3:0, 22.2:1}

IMAGE_REJECTION_MODES = {'both':0, 'high':1, 'low':2}

DECIM_MAX = 16
DECIM_MIN = 1

SENSITIVITY_MIN = 0
SENSITIVITY_MAX = 2

ATTENS = [0, 5, 10, 15]


class SignalHound:
    def __init__(self, cal_file_name=CAL_FILE_NAME):
        self.log = logging.getLogger('SignalHound')
        self.log.debug('initializing')

        if not os.path.exists(cal_file_name) or True:
            self.log.info('creating new calibration file')
            SHAPI.Initialize()
            self.save_cal_data(cal_file_name)
        else:
            cal = self.load_cal_data(cal_file_name)

        self.config = DEFAULT_CONFIG.copy()
        SHAPI.ConfigureFast(**self.config)

        self.fft_size = 512
        self.set_image_rejection('both')
        self.sweep_mode = 'fast'
        self.desired_rbw = 1

    def save_cal_data(self, cal_file_name):
        self.log.debug('retrieving calibration table')
        cal = SHAPI.CopyCalTable()

        with open(cal_file_name, 'wb') as fh:
            pickle.dump(list(cal), fh)

        self.log.debug('wrote to calibration file')

    def load_cal_data(self, cal_file_name):
        self.log.debug('loading calibration file')

        with open(cal_file_name, 'rb') as fh:
            data = pickle.load(fh)

        cal = (ctypes.c_ubyte * len(data))(*data)
        SHAPI.InitializeEx(cal)

    def get_spectrum(self, start_freq, stop_freq):
        start_freq *= 1e6
        stop_freq *= 1e6

        if start_freq < MIXER_LOW_BAND_EDGE < stop_freq:
            raise Exception('frequency span cannot cross mixer bands (at %s MHz)' % MIXER_LOW_BAND_EDGE)

        if start_freq > MIXER_LOW_BAND_EDGE:
            self.set_mixer_band('high')
        else:
            self.set_mixer_band('low')

        self.log.debug('retrieving sweep')
        start_time = time.time()

        if self.sweep_mode == 'slow':
            # use avg_count to make avg_count*fft_size multiple of 512
            avg_count = max(1, 512//self.fft_size)
            if avg_count > 1:
                self.log.info('%d sweeps will be averaged for correct RBW' % avg_count)

            buff_size = SHAPI.GetSlowSweepCount(start_freq, stop_freq, self.fft_size)
            count, sweep = SHAPI.GetSlowSweep(start_freq, stop_freq, buff_size, self.fft_size,
                                        avg_count, self.image_handling)
        else:
            # set required parameters for fast sweeps
            self.set_decim(1)
            self.set_adc_clock(23.3)
            self.set_if_path(10.7)

            buff_size = SHAPI.GetFastSweepCount(start_freq, stop_freq, self.fft_size)
            #print 'BUFF_SIZE:', buff_size, self.fft_size

            count, sweep = SHAPI.GetFastSweep(start_freq, stop_freq, buff_size, self.fft_size,
                                        self.image_handling)

        self.log.debug('sweep time: %0.1f s' % (time.time() - start_time))

        assert(buff_size == count)

        return asarray(sweep)

    def set_sweep_mode(self, mode):
        if self.sweep_mode != mode:
            self.log.debug('setting sweep mode to: %s' % mode)

            self.sweep_mode = mode
            self.set_rbw(self.desired_rbw)

    def get_iq(self, center_freq, num_samples):
        center_freq *= 1e6

        self.log.debug('retrieving I/Q samples')
        centerFreq, i_buff, q_buff = SHAPI.GetIQDataPacket(center_freq, num_samples)
        iq = asarray(i_buff, dtype='complex') + 1j*asarray(q_buff, dtype='complex')

        return centerFreq/1e6, iq

    def set_mixer_band(self, band):
        self.config['mixerBand'] = MIXER_BANDS[band]

        self.log.debug('setting mixer band to: %s' % band)
        SHAPI.ConfigureFast(**self.config)

    def set_image_rejection(self, mode):
        try:
            self.image_handling = IMAGE_REJECTION_MODES[mode]
        except KeyError:
            raise Exception('bad image rejection mode')

        self.log.debug('setting image rejection mode to: %s' % mode)

    def set_if_path(self, path):
        self.config['IF_Path'] = IF_PATHS[path]

        self.log.debug('setting IF path to: %s MHz' % path)
        SHAPI.ConfigureFast(**self.config)

    def set_adc_clock(self, clock):
        self.config['ADC_clock'] = ADC_CLOCKS[clock]

        self.log.debug('setting ADC clock to: %s MHz' % clock)
        SHAPI.ConfigureFast(**self.config)

    def set_sensitivity(self, sensitivity):
        if SENSITIVITY_MIN <= sensitivity <= SENSITIVITY_MAX:
            self.config['sensitivity'] = sensitivity
        else:
            raise Exception('bad sensitivity value')

        self.log.debug('setting sensitivity to: %d' % sensitivity)
        SHAPI.ConfigureFast(**self.config)

    def set_decim(self, decim):
        if DECIM_MIN <= decim <= DECIM_MAX:
            self.config['decimation'] = decim
        else:
            raise Exception('bad decimation value')

        self.log.debug('setting decimation to: %d' % decim)
        SHAPI.ConfigureFast(**self.config)

    def set_atten(self, atten):
        if atten in ATTENS:
            self.config['attenVal'] = atten
        else:
            raise Exception('bad attenuation value')

        self.log.debug('setting attenuation to: %d' % atten)
        SHAPI.ConfigureFast(**self.config)

    def set_rbw(self, rbw):
        enb_factor = 3.37
        self.desired_rbw = rbw

        rbw *= 1e3

        if self.sweep_mode == 'fast':
            fft_exps = range(4, 8 + 1)
            decims = [1]
        else:
            fft_exps = range(4, 16 + 1)
            decims = range(DECIM_MIN, DECIM_MAX+1)

        alpha = enb_factor*FS/rbw

        best_decim = decims[0]
        best_n = fft_exps[0]
        best_err = abs(alpha - best_decim*2**best_n)

        for n in fft_exps:
            for decim in decims:
                cur_err = abs(alpha - decim*2**n)

                if cur_err < best_err:
                    best_err = cur_err
                    best_decim = decim
                    best_n = n

        fft_size = 2**best_n
        rbw_actual = enb_factor*FS/(fft_size*best_decim)

        if self.sweep_mode == 'fast' and abs(POWER_BANDWIDTH - rbw) < abs(rbw - rbw_actual):
            fft_size = 1
            rbw_actual = POWER_BANDWIDTH
            err_per = 0
        else:
            err_per = 100*abs(rbw_actual - rbw)/rbw

        self.log.debug('required FFT size: %d' % fft_size)
        msg = 'resolution bandwidth set to: %0.1f kHz (error: %.1f%%)' % (rbw_actual/1e3, err_per )
        if err_per > 10:
            self.log.warn(msg)
        else:
            self.log.debug(msg)

        self.set_decim(best_decim)
        self.fft_size = fft_size

def main():
    start_freq, stop_freq = 10, 10.2

    sh = SignalHound()

    if 1:
        import time

        sh.fft_size = 1

        start_time = time.time()
        freqs = arange(152, 452, 0.2)
        powers = sh.get_spectrum(freqs[0], freqs[-1])
        #powers = [mean(abs(sh.get_iq(f, 1*512)[1])**2) for f in freqs]

        print 'took:', time.time() - start_time

        figure()
        plot((powers))

    if 0:
        sh.set_atten(15)
        sh.set_rbw(100e3, 'fast')
        d = [sh.get_spectrum(start_freq, stop_freq, mode='fast', avg_count=1) for i in range(5)]
        f = linspace(start_freq, stop_freq, len(d))

        figure()
        #plot(f, d)
        imshow(d, aspect='auto')

    if 0:
        sh.set_sweep_mode('fast')
        sh.set_rbw(1)
        #sh.fft_size = 1024*1
        sh.set_atten(0)
        sh.set_sensitivity(1)

        x = sh.get_spectrum(start_freq, stop_freq)

        f = linspace(start_freq, stop_freq, len(x))

        figure()
        plot(f, x)

    show()

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    main()