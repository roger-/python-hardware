from __future__ import division
import time
import visa
from pyvisa import vpp43

# Python interface for HP 8657A signal generator (HP-IB)


class SignalGenerator(object):
    MAX_SETTLING_TIME = 30e-3
    MAX_CHARS = 9

    def __init__(self, name=None, wait_for_settle=True, reset=True):
        self.wait_for_settle = wait_for_settle

        if not name:
            instruments = visa.get_instruments_list()

            # find first GPIB interface
            for dev in instruments:
                if "gpib" in dev.lower():
                    name = dev
                    break
            else:
                raise exception('cannot find device')

        # connect to device and configure VISA settings
        self.device = visa.instrument(name)
        vpp43.gpib_control_ren(self.device.vi, visa.VI_GPIB_REN_ASSERT_ADDRESS) # doesn't work without this
        self.device.clear()
        
        self.set_output_enabled(False)
        if reset:
            self.reset()

    def reset(self):
        self.device.write('DLC')
        self.settle_output()

    def set_freq(self, freq_hz):
        freq_mhz = freq_hz/1e6
        self.device.write('FR %s MZ' % self._val_to_dev_str(freq_mhz, 10))
        self.settle_output()

    def set_power(self, power_dbm):
        self.device.write('AP %s DM' % self._val_to_dev_str(power_dbm, 9))
        self.settle_output()

    def settle_output(self):
        if self.wait_for_settle and self.output_enabled:
            time.sleep(self.MAX_SETTLING_TIME)

    def set_output_enabled(self, enabled=False):
        if enabled:
            self.output_enabled = True
            cmd = 'R3'
        else:
            self.output_enabled = False
            cmd = 'R2'
        self.device.write(cmd)
        self.settle_output()

    def __del__(self):
        pass
        #self.set_output_enabled(False)

    def _val_to_dev_str(self, val, max_chars=MAX_CHARS):
        val_as_str = '%0.9f' % val

        return val_as_str[:max_chars]


if __name__ == '__main__':
    gen = SignalGenerator()

    time.sleep(3)

    print 'Configuring instrument'
    gen.set_freq(123e6)
    gen.set_power(-30)

    print 'Enabling output'
    gen.set_output_enabled(True)
    
    print 'Testing frequency/power'
    
    for f in range(95, 105, 2):
        gen.set_freq(f*1e6)
        
        for p in [-80]:
            gen.set_power(p)
            #time.sleep(1)

    print 'Disabling output'
    #gen.set_output_enabled(False)