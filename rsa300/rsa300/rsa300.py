from __future__ import division
from ctypes import *
import api
import numpy as np


class RSA300Base(object):
    def __init__(self, dev_id=None, reset=True):
        if dev_id is None:
            id_list = self.find_devices()

            if not id_list:
                raise Exception('could not find RSA')

            # use first device
            dev_id = id_list[0]

        self.dev_id = dev_id
        self.data_buffer = []

        api.Connect(self.dev_id)

        if reset:
            self.reset()

    def find_devices(self):
        MAX_DEVICES = 10

        id_list = (c_int * MAX_DEVICES)()
        dev_serial = POINTER(POINTER(c_wchar))()
        num_found = c_int(0)

        api.Search(id_list, (dev_serial), byref(num_found))

        return id_list[:num_found.value]

    def acquire(self, val=True):
        if val:
            api.Run()
        else:
            api.Stop()

    def get_center_freq(self):
        cf = c_double(0)

        api.GetCenterFreq(byref(cf))

        return cf.value

    def set_center_freq(self, cf):
        api.SetCenterFreq(cf)

    def get_ref_level(self):
        rl = c_double(0)

        api.GetReferenceLevel(byref(rl))

        return rl.value

    def set_ref_level(self, rl):
        api.SetReferenceLevel(rl)

    def get_device_info(self):
        BUFFER_LEN = 50

        info = {}
        buff = (c_char * BUFFER_LEN)()

        api.GetDeviceNomenclature(buff)
        info['name'] = buff.value

        api.GetAPIVersion(buff)
        info['api_version'] = buff.value

        api.GetDeviceSerialNumber(buff)
        info['serial_number'] = buff.value

        api.GetFirmwareVersion(buff)
        info['firmware_version'] = buff.value

        api.GetFPGAVersion(buff)
        info['fpga_version'] = buff.value

        api.GetHWVersion(buff)
        info['hw_version'] = buff.value

        return info

    def self_test(self):
        api.POST_QueryStatus()

    def reset(self):
        api.Preset()

    def reboot(self):
        api.ResetDevice(False)

    def close(self):
        api.acquire(False)
        api.Disconnect()

    center_freq = fc = property(get_center_freq, set_center_freq)
    ref_level = property(get_ref_level, set_ref_level)
    device_info = property(get_device_info)

class RSA300IQ(RSA300Base):
    def __init__(self, *args, **kwargs):
        RSA300Base.__init__(self,  *args, **kwargs)

        api.SPECTRUM_SetEnable(False)

    def wait_for_data(self, timeout_ms=1000):
        ready = c_bool(False)

        api.WaitForIQDataReady(timeout_ms, byref(ready))

        if not ready:
            raise Exception('timeout waiting for data')

    def set_bandwidth(self, bw):
        api.SetIQBandwidth(bw)

    def get_bandwidth(self):
        bw = c_double(0)

        api.GetIQBandwidth(byref(bw))

        return bw.value

    def set_record_len(self, length):
        api.SetIQRecordLength(length)

    def get_record_len(self):
        rl = c_long(0)

        api.GetIQRecordLength(byref(rl))

        return rl.value

    def get_data(self, num_points, timeout_ms=1000, acquire=True):
        if len(self.data_buffer) < num_points*2:
            self.data_buffer = (c_float * max_points*2)()

        if acquire:
            self.acquire(True)
            
        if timeout_ms is not None:
            ready = self.wait_for_data(timeout_ms)

            if not ready:
                raise Exception('measuurement timeout')

        api.GetIQData(self.data_buffer, 0, num_points*2)

        iq = np.empty(num_points, 'complex')
        iq.real, iq.imag = self.data_buffer[:num_points:2], self.data_buffer[1:num_points:2]

        return iq

    def reset(self):
        RSA300Base.reset(self)
        api.SPECTRUM_SetEnable(False)

    bandwidth = property(get_bandwidth, set_bandwidth)
    record_len = property(get_record_len, set_record_len)

class RSA300Spectrum(RSA300Base):
    def __init__(self, *args, **kwargs):
        RSA300Base.__init__(self,  *args, **kwargs)

        api.SPECTRUM_SetEnable(True)

    def wait_for_data(self, timeout_ms=1000):
        ready = c_bool(False)

        api.SPECTRUM_WaitForDataReady(timeout_ms, byref(ready))

        return ready

    def set_detector(self, trace_num=1, detector_type=api.SpectrumDetector_PosPeak):
        # TODO: disable traces
        api.SPECTRUM_SetTraceType(trace_num, True, detector_type)

    def get_data(self, trace_num=1, max_points=64001, timeout_ms=5000, acquire=True):
        if len(self.data_buffer) < max_points:
            self.data_buffer = (c_float * max_points)()

        num_points = c_int(0)

        if acquire:
            self.acquire(True)

        if timeout_ms is not None:
            ready = self.wait_for_data(timeout_ms)

            if not ready:
                raise Exception('measurement timeout')

        api.SPECTRUM_GetTrace(trace_num, max_points, self.data_buffer, byref(num_points))

        return np.array(self.data_buffer[:num_points.value])

    def get_settings(self):
        ss = api.Spectrum_Settings()

        api.SPECTRUM_GetSettings(byref(ss))

        return dict((field, getattr(ss, field)) for field, _ in ss._fields_)

    def update_settings(self, **settings):
        VALID_SETTINGS = ['span', 'enableVBW', 'rbw', 'traceLength', 'verticalUnit', 'window', 'vbw']

        new_settings = self.get_settings()
        new_settings.update(settings)

        # make sure all elements are ints and valid
        new_settings = {key: int(val) for key, val in new_settings.iteritems() if key in VALID_SETTINGS}
        
        ss = api.Spectrum_Settings(**new_settings)
        api.SPECTRUM_SetSettings(ss)

    def configure(self, **params):
        DETECTORS = {'pos': api.SpectrumDetector_PosPeak,
                     'neg': api.SpectrumDetector_NegPeak,
                     'avg': api.SpectrumDetector_AverageVRMS,
                     'sample': api.SpectrumDetector_Sample}
        MIN_TRACE_LEN, MAX_TRACE_LEN = 801, 64001

        settings = {}

        if 'start_freq' in params:
            settings['span'] = params['stop_freq'] - params['start_freq']
            center_freq = (params['stop_freq'] + params['start_freq']) / 2

            assert(settings['span'] > 0)

            self.set_center_freq(center_freq)
            
        if 'center_freq' in params:
            self.set_center_freq(params['center_freq'])

        if 'span' in params:
            settings['span'] = params['span']
            
        if 'ref_level' in params:
            self.set_ref_level(params['ref_level'])

        if 'rbw' in params:
            settings['rbw'] = params['rbw']

        if 'vbw' in params:
            if params['vbw']:
                settings['vbw'] = params['vbw']
                settings['enableVBW'] = True
            else:
                settings['enableVBW'] = False

        if 'detector' in params:
            self.set_detector(1, DETECTORS[params['detector']])

        # adjust the trace length
        if 'start_freq' in params and 'rbw' in params:
            settings['traceLength'] = settings['span'] // settings['rbw']

            # traceLength must be odd
            if not settings['traceLength'] % 2:
                settings['traceLength'] -= 1

            # clip
            if settings['traceLength'] < MIN_TRACE_LEN:
                settings['traceLength'] = MIN_TRACE_LEN
            elif settings['traceLength'] > MAX_TRACE_LEN:
                settings['traceLength'] = MAX_TRACE_LEN

        self.update_settings(**settings)

    def reset(self):
        RSA300Base.reset(self)
        api.SPECTRUM_SetEnable(True)
        api.SPECTRUM_SetDefault()

        # this should be set by default, but isn't?
        self.set_detector(1, api.SpectrumDetector_PosPeak)


def test():
    tek = RSA300Spectrum()

    tek.configure(rbw=1e3, start_freq=100e6, stop_freq=200e6, detector='pos')

    print tek.get_settings()
    print tek.get_data()

if __name__ == '__main__':
    test()
