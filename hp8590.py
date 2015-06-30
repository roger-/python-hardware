from __future__ import division
import numpy as np
import logging
import datetime
import time
import visa
import struct
from contextlib import contextmanager

logging.basicConfig()
log = logging.getLogger(name=__name__)
log.setLevel(logging.DEBUG)

# TODO: verify auto-coupling
#       string settings for properties
#       fix timeouts
#       fix cmd err: "M; M;"

class BaseSpectrumAnalyzer(object):
    def send_cmds(self, cmds):
        cmd_str = ';'.join(cmds)

        if len(cmd_str) > self.MAX_CMD_CHARS:
            raise Exception('command string too long: ' + cmd_str)

        self.send_cmd(cmd_str)

    def send_cmd(self, cmd_str):
        cmd_str = cmd_str.upper()

        if self.use_queue:
            self.cmd_queue.append(cmd_str)
        else:
            log.debug('sending string: ' + cmd_str + ';')
            self.instrument.write(cmd_str + ';')

    def send_query(self, query_str):
        query_str = query_str.upper() + ';'
        log.debug('sending query: ' + query_str)

        return self.instrument.query(query_str).strip().lower()

    @contextmanager
    def queued_cmds(self):
        self.cmd_queue = []
        self.use_queue = True
        yield

        self.use_queue = False
        if self.cmd_queue:
            self.send_cmds(self.cmd_queue)

        self.cmd_queue = []

class SpectrumAnalyzer(BaseSpectrumAnalyzer):
    MAX_SAMPLE_POINTS = 401
    MAX_CMD_CHARS = 2047
    TIMEOUT_INIT = 5*1000
    TIMEOUT_MEASURE = 110*1000

    def __init__(self, port="auto", reset=True, use_bytes=False):
        self.use_queue = False
        self.cmd_queue = []
        self.use_bytes = False

        self.rm = visa.ResourceManager()

        '''Initialize spectrum analyzer'''
        if port == "auto":
            # use first GPIB device found
            devices = self.rm.list_resources()

            for dev in devices:
                if "gpib" in dev.lower():
                    port = dev
                    break

        # initialize device
        self.instrument = self.rm.open_resource(port, timeout=self.TIMEOUT_INIT)

        if reset:
            self.reset()
            #self.clear_trace()

        self.set_output_format(use_bytes)

        info = self.get_info()
        log.info("initialized {model} (serial #: {serial_number}, firmware: {firmware_date}, uptime: {uptime.days} days)".format(**info))

        self.instrument.timeout = self.TIMEOUT_MEASURE

    def set_output_format(self, use_bytes=False):
        self.use_bytes = use_bytes

        with self.queued_cmds():
            # use binary format for data
            self.send_cmd('TDF B')

            if use_bytes:
                self.send_cmd('MDS B')
            else:
                self.send_cmd('MDS W')

    def reset(self):
        log.debug('resetting')

        with self.queued_cmds():
            # preset state
            self.send_cmd('IP')

            # single sweep mode
            self.send_cmd('SNGLS')

            # set date/time and display on instrument
            datetime_str = datetime.datetime.now().strftime('%y%m%d%H%M%S')
            self.send_cmd('TIMEDATE ' + datetime_str)
            self.send_cmd('TIMEDSP ON')

            self.instrument.clear()

        # configure PyVISA for binary data
        # TODO

    def get_info(self):
        info = {}

        # get model/firmware info
        info['model'] = self.send_query('ID?').strip()
        info['firmware_date'] = self.send_query('REV?') #firmware date
        info['serial_number'] = self.send_query('SER?') #firmware date

        # get uptime
        uptime_str = self.send_query('PWRUPTIME?').strip() # in ms
        info['uptime'] = datetime.timedelta(seconds=float(uptime_str)/1e3)

        return info

    def get_trace(self, trace='a', ref_level=None):
        # read binary data
        self.send_cmd('TS;T{}?'.format(trace))
        data = self.instrument.read_raw()

        if ref_level is None:
            ref_level = self.ref_level

        # unpack and convert to dB
        if self.use_bytes:
            trace = np.asarray(struct.unpack('>401B', data))
            trace = (trace * 32 - 8000) * 0.01 + ref_level
        else:
            trace = np.asarray(struct.unpack('>401H', data)) # B H
            trace = (trace - 8000) * 0.01 + ref_level

        return trace

    def get_sweeps(self, num, trace='a', delay=0):
        ref_level = self.ref_level

        times = []
        sweeps = []

        for i in range(num):
            log.info('starting sweep {} of {}'.format(i+1, num))
            t = time.time()
            spectrum = self.get_trace(trace, ref_level=ref_level)
            log.debug('sweep done in {} ms'.format((time.time() - t)*1e3))

            times.append(t)
            sweeps.append(spectrum)

            if i < (num - 1) and delay:
                log.debug('waiting {} ms'.format(delay*1e3))
                time.sleep(delay)

        return times, sweeps

    @property
    def trigger_level(self):
        trigger = self.send_query('TM?')
        
        if trigger == 'vid':
            return float(self.send_query('DL?'))        
        else:
            return None

    @trigger_level.setter
    def trigger_level(self, level=None, unit='dBm'):
        cmd_list = []

        with self.queued_cmds():
            if level is None:
                self.send_cmd('TM FREE')
            else:
                self.send_cmd('TM VID')
                self.send_cmd('DL {}{}'.format(level, unit))

    def clear_trace(self, trace='A'):
        self.send_cmd('CLRW TR' + trace)

    @contextmanager
    def temp_context(self):
        self.send_cmd('SAVES 1')
        yield
        self.send_cmd('RCLS 1')

    def make_properties(cmd_get, unit='', cmd_set=None, value_map=None, verify_val=True, return_type=float):
        if not cmd_set:
            cmd_set = cmd_get

        def _get(self):
            #TODO: invert value_map?
            val = self.send_query(cmd_get + '?')
            return return_type(val)

        def _set(self, val):
            val = str(val).lower()
            if value_map:
                val = value_map[val].lower()

            cmd = cmd_set + ' ' + val + ' ' + unit

            self.send_cmd(cmd)

            if verify_val and val.lower() != 'auto':
                retval = self.send_query(cmd_get + '?').lower()

                if return_type(retval) != return_type(val):
                    raise Exception('value set to {}, not expected {}'.format(retval, val))

            return

        return _get, _set

    freq_center = property(*make_properties('CF', unit='Hz'))
    freq_span = property(*make_properties('SP', unit='Hz'))
    freq_start = property(*make_properties('FA', unit='Hz'))
    freq_stop = property(*make_properties('FB', unit='Hz'))

    sweep_time = property(*make_properties('ST', unit='sc'))
    bw_res = property(*make_properties('RB', unit='Hz'))
    bw_vid = property(*make_properties('VB', unit='Hz'))

    atten = property(*make_properties('AT', unit='dBm'))
    ref_level = property(*make_properties('RL', unit='dBm'))

    status_byte = property(*make_properties('STB',cmd_set='RSQ', return_type=int, verify_val=False))

    VAL_MAP_DET = {'positive': 'POS', 'negative': 'NEG', 'sample': 'SMP'}
    detector = property(*make_properties('DET', unit='', return_type=str, value_map=VAL_MAP_DET, verify_val=False))


def benchmark():
    import time
    import numpy as np
    import pylab as pyl

    sa = SpectrumAnalyzer(reset=0, use_bytes=1)

    sa.freq_center = 2.420e3
    sa.freq_span = 20
    #sa.bw_res = 100

    times = []

    ref_level = sa.ref_level

    for i in range(300):
        start = time.time()
        sa.get_trace(ref_level=ref_level)
        dur = time.time() - start
        times.append(dur)

    print 'mean time:', np.mean(times), np.std(times)


    pyl.hist(times, 200)

    pyl.show()

def main():
    sa = SpectrumAnalyzer(reset=0, use_bytes=1)

    sa.freq_center = 2.850e9
    sa.freq_span = 20e6
    sa.bw_res = 200e3
    sa.sweep_time = 100e-3


    sa.set_trigger(None)

    import pylab as pyl


    sa.clear_trace()


    pyl.plot(sa.get_trace())

    pyl.show()

    if 0:

        for i in range(5):
            pyl.plot(sa.get_trace())

        pyl.show()

    #print sa.get_trace()

if __name__ == '__main__':
    main()