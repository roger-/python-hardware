from __future__ import division
from rsa300 import RSA300Spectrum


def test():
    tek = RSA300Spectrum()

    tek.configure(rbw=1e3, start_freq=100e6, stop_freq=200e6, detector='pos')

    print tek.get_settings()
    print tek.get_data()

if __name__ == '__main__':
    test()
