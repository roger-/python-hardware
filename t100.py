from __future__ import division
import serial
from numpy import *
import pylab as plt

plt.ioff()

class T100:
    BAUD = 38400
    TIMEOUT = 2
    CMD_DISABLE = "D"
    CMD_START_MEAS = "S"
    FREQ_RES = 25e3

    def __init__(self, port="COM3", start_freq=100e6):
        '''Initialize T100
        port -> COM port
        return -> None'''

        self.port = serial.Serial(port, self.BAUD, timeout=self.TIMEOUT)

        ## make sure T100 is connected and working
        try:
            self.set_freq(start_freq)
            self.get_s11()
        except ValueError:
            raise Exception("Cannot communicate with T100")

    def set_freq(self, freq):
        '''Tune to frequency
        freq -> frequency in Hz
        return -> None'''

        ## verify frequency range
        if not ((100e6 <= freq <= 170e6) or (400e6 <= freq <= 470e6)):
            raise Exception("Invalid frequency range")

        if (freq % self.FREQ_RES) != 0:
            print "Warning: frequency value invalid, rounding"
            freq = round(freq/self.FREQ_RES)*self.FREQ_RES

        ## convert to kHz and send to T100
        freq_cmd = "%d" % (freq/1e3)
        self.port.write(freq_cmd)

        return

    def get_s11(self):
        '''Measure S11 at current frequency
        return -> S11 in complex form'''

        ## send measurement command and get data
        self.port.write(self.CMD_START_MEAS)
        data = self.port.readline()

        ## extract numbers from strings and convert to complex form
        (s11_mag, s11_arg_deg) = [float(s) for s in data.strip().split(',')]
        s11_arg = 2*pi*s11_arg_deg/360           ## convert to radians
        s11 = s11_mag*exp(1j*s11_arg)        ## convert to complex form

        return s11

    def measure_freq(self, freq, avg_len=1):
        '''Measure S11 at specified frequency, with averaging
        freq -> frequency in Hz
        avg_len -> number of samples to average
        return -> average S11 in complex form'''

        ## tune to frequency
        self.set_freq(freq)

        ## average over frequency
        s11 = array([self.get_s11() for i in xrange(avg_len)]).mean()

        return s11

    def measure_freq_range(self, freqs, avg_len=1):
        '''Measure S11 at specified frequencies, with averaging
        freqs -> array of frequencies in Hz
        avg_len -> number of samples to average
        return -> average S11 values in complex form'''

        return array([self.measure_freq(freq, avg_len) for freq in freqs])

    def disable(self):
        '''Disable output
        return -> None'''

        self.port.write(self.CMD_DISABLE)

    def __del__(self):
        self.disable()          ## disable output

def s11_to_z11(s11, Z0=50):
    return Z0*(1 + s11)/(1 - s11)

def resolve_z(z, freq, form='series'):
    if form == 'series':
        res = real(z)
        x = imag(z)
    elif form == 'parallel':
        y = 1/z
        res = 1/real(y)
        x = 1/imag(y)

    w = 2*pi*freq
    ind = x/w
    cap = -1/(w*x)

    q = abs(imag(z)/real(z))

    return {'r':res, 'l':ind, 'c':cap, 'x':x, 'q':q}

def main():
    start = 100e6
    stop = 170e6
    step = 1e6

    t = T100()
    fs = arange(start, stop+step, step)

    s11 = t.measure_freq_range(fs, 1)
    z = s11_to_z11(s11)
    Ls = resolve_z(z, fs, 'series')['l']

    plt.figure()
    plt.plot(fs, Ls)


    #plt.polar(2*pi*s11[:, 1]/360, s11[:, 0])
    #plt.ylim(49, 51)
    #plt.figure()
    #plt.polar(2*pi*s11[:, 1]/360, s11[:, 0])
    #plt.plot(-1/(2*pi*fs*1e6*imag(z11)))

    plt.show()

if __name__ == "__main__":
    main()




