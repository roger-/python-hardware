A Python wrapper for the Tektronix RSA306 spectrum analyzer.

# Installation

So far this only works with Windows. Make sure the RSA300API.dll file is available in your system path!

# Usage

The `rsa300.RSA300Spectrum` and `rsa300.RSA300IQ` classes provide access to the spectrum analyzer and IQ
functionality of the device, respectively.

Sample usage:

```python
tek = RSA300Spectrum()

tek.configure(rbw=1e3, start_freq=100e6, stop_freq=200e6, detector='pos')

print tek.get_settings()
print tek.get_data()
```

A one-to-one ctypes wrapper for the case API is available in `rsa300.api` (automatically generated
using ctypesgen).

