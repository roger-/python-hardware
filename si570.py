from __future__ import division
import struct
import usb, time
import logging

def find_usb_device(vendor_id, product_id):
    for bus in usb.busses():
        for device in bus.devices:
            if device.idVendor == vendor_id and device.idProduct == product_id:
                return device

    return None

class Si570:
    USB_VENDOR_ID = 0x16C0
    USB_PRODUCT_ID = 0x05DC

    USB_BUFFER_SIZE = 254
    USB_REQUEST_DIRS = {'out': usb.TYPE_VENDOR | usb.RECIP_DEVICE | usb.ENDPOINT_OUT,
                        'in':usb.TYPE_VENDOR | usb.RECIP_DEVICE | usb.ENDPOINT_IN}

    CMD_SET_FREQ = 0x32
    CMD_GET_FREQ = 0x3A
    CMD_GET_TEMP = 0x42

    F_MAX = 269

    def __init__(self):
        self.log = logging.getLogger('main.si570')

        self.log.debug('looking for Si570')
        self.device = find_usb_device(self.USB_VENDOR_ID, self.USB_PRODUCT_ID)

        if not self.device:
            raise Exception('device not available')
        else:
            self.log.debug('device found')

        self.handle = self.device.open()

    def _send_cmd(self, cmd, param0=0, param1=0, buffer=USB_BUFFER_SIZE, dir='out'):
        val = self.handle.controlMsg(requestType=self.USB_REQUEST_DIRS[dir], request=cmd,
                                     value=param0, index=param1, buffer=buffer)

        return val

    def set_freq(self, freq):
        if freq > self.F_MAX:
            raise Exception('freq = %f MHz is beyond maximum frequency (%f MHz)' % (freq, self.F_MAX))

        self.log.debug('setting frequency to %f MHz' % freq)
        freq_encoded = struct.pack('I', int(freq * 2**21))
        bytes_written = self._send_cmd(self.CMD_SET_FREQ, buffer=freq_encoded, dir='out')

    def get_freq(self):
        self.log.debug('retrieving frequency')
        freq_encoded = self._send_cmd(self.CMD_GET_FREQ, buffer=4, dir='in')

        if len(freq_encoded) != 4:
            raise Exception('error getting frequency')

        freq_encoded_str = ''.join(chr(x) for x in freq_encoded)
        freq = struct.unpack('L', freq_encoded_str)[0]/(2**21)

        return freq

    def get_temp(self):
        self.log.debug('retrieving temperature')
        temp_encoded = self._send_cmd(self.CMD_GET_TEMP, buffer=2, dir='in')

        if len(temp_encoded) != 2:
            raise Exception('error getting temperature')

        temp_encoded_str = ''.join(chr(x) for x in temp_encoded)
        temp = struct.unpack('H', temp_encoded_str)[0]/(2**4)

        return temp

def main2():
    si = Si570()

    from numpy import linspace

    errs = []
    for freq in linspace(30, 35, 1000):
        si.set_freq(freq)
        err = 1e6*(freq - si.get_freq())
        errs.append(err)

        #time.sleep(2)

    print max(errs), mean(errs)

def main():
    si = Si570()

    si.set_freq(50)

    print si.get_temp()

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    main()
