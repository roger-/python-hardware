# Python interfaces for Yaesu GS-232A and Rotor-EZ antenna rotor serial computer interface
#

from __future__ import division
import serial
import logging
from common import threadmethod, memoize_args
import time

class Rotor(object):
        _cur_angle = None
        _port = None

        def __init__(self, *args, **kwargs):
                '''Initialize rotor on serial port'''
                class_name = self.__class__.__name__
                self._log = logging.getLogger(name="main." + str(class_name)) # TODO: doesn't give the right name
                self._port = serial.Serial(*args, **kwargs)

                self._log.debug("device initialized")

        def __del__(self):
                self._port.close()

                self._log.debug("port closed")

        def __repr__(self):
                return "<rotor on " + self._port.portstr + ", angle = " + str(self.get_angle()) + ">"

        def _send_cmd(self, cmd):
                '''send command to rotor'''
                self._port.write(cmd + "\r\n")
                time.sleep(self.ROTOR_DELAY) # sending commands too fast may cause errors

        def get_angle(self):
                 raise NotImplementedError

        def _set_angle_async(self, angle):
                 raise NotImplementedError

        @threadmethod(60) # timeout after 60s. TODO: might be too short for low speeds
        def wait_for_angle(self, angle):
                '''Wait until rotor is at given angle'''
                self._log.info("waiting for rotor")

                start_time = time.time()
                while True:
                        # find distance from desired angle (0-360 degrees)
                        curr_angle = self.get_angle()
                        tmp = abs(curr_angle - angle)
                        dist = min(tmp, 360-tmp)

                        if dist <= self.ANGLE_TOLERANCE:
                                break

                self._log.info("waited %0.2fs" % (time.time()-start_time))

        def set_angle_async(self, angle):
                self._log.debug("moving to %d degrees" % angle)

                self._set_angle_async(angle)

        @memoize_args("angle")
        def set_angle(self, angle):
                '''rotate to given angle (in degrees)'''
                self.set_angle_async(angle)
                self.wait_for_angle(angle)

        angle = property(get_angle)


class RotorEZ(Rotor):
        '''Simple serial port wrapper class for antenna rotor. TODO: add error checking!'''
        ERROR_STRING = "?>"
        ANGLE_TOLERANCE = 2
        ROTOR_DELAY = 50e-3
        BAUD_RATE = 4800
        TIMEOUT = 2 # responses take up to 1.8s (!)

        CMD_GET_ANGLE = "AI1"
        CMD_SET_ANGLE = "AP1"

        def __init__(self, port="COM1"):
                '''Initialize rotor on serial port'''
                Rotor.__init__(self, port, baudrate=self.BAUD_RATE, timeout=self.TIMEOUT)

        def get_angle(self):
                '''get current angle of rotor (in degrees)'''
                self._send_cmd(self.CMD_GET_ANGLE)

                # read reply and extract angle
                val = self._port.readline().strip()
                direction = val[1:] # skip ";" in response

                return int(direction)

        def _set_angle_async(self, angle):
                '''start rotating to given angle (in degrees)'''
                param = "%03d" % angle
                self._send_cmd(self.CMD_SET_ANGLE + param)

class RotorGS(Rotor):
        '''Simple serial port wrapper class for antenna rotor. TODO: add error checking!'''
        ERROR_STRING = "?>"
        ANGLE_TOLERANCE = 2
        ROTOR_DELAY = 10e-3
        BAUD_RATE = 9600
        TIMEOUT = 1

        CMD_GET_ANGLE = "C"
        CMD_SET_ANGLE = "M"
        CMD_STOP = "S"
        CMD_SET_SPEED = "X"
        CMD_PROGRAM = "M"
        CMD_PROGRAM_GO = "T"
        CMD_ROTATE_LEFT = "L"
        CMD_ROTATE_RIGHT = "R"

        def __init__(self, port="COM1"):
                '''Initialize rotor on serial port'''
                Rotor.__init__(self, port, baudrate=self.BAUD_RATE, timeout=self.TIMEOUT)

                self.stop()
                self.set_speed(4)

        def stop(self):
                '''stop rotor'''
                self._log.debug("stopping rotor")
                self._send_cmd(self.CMD_STOP)

        def rotate(self, direction):
                '''turn rotor in given direction ("CW" for clockwise and "CCW" for counter-clockwise)'''
                DIRECTION_KEYS = {"CCW":self.CMD_ROTATE_LEFT, "CW":self.CMD_ROTATE_RIGHT}
                cmd = DIRECTION_KEYS[direction]
                self._send_cmd(cmd)

        def set_speed(self, speed):
                '''set rotor speed (1-4)'''
                cmd = self.CMD_SET_SPEED + str(speed)
                self._send_cmd(cmd)

        def get_angle(self):
                '''get current angle of rotor (in degrees)'''
                self._send_cmd(self.CMD_GET_ANGLE)

                # read reply and extract angle
                val = self._port.readline().strip()
                direction = val[1:]

                return int(direction)

        def _set_angle_async(self, angle):
                '''start rotating to given angle (in degrees)'''
                param = "%03d" % angle
                self._send_cmd(self.CMD_SET_ANGLE + param)

        def program(self, delay, angles):
                '''program rotor to step between angles (in degrees) with given time delay (in seconds) in between steps.
                   Automatically rotates to first angle value and awaits a go() command'''
                cmd = "%s%03d" % (self.CMD_PROGRAM, delay)
                for angle in angles:
                        cmd += (" %03d" % angle)

                self._send_cmd(cmd)

        def go(self):
                '''start sequence following program() call'''
                self._log.debug("starting programmed sequence")
                self._send_cmd(self.CMD_PROGRAM_GO)

        speed = property(None, set_speed)



def measure_speed(r):
        time_res = 0
        angle_res = 3

        r.set_angle(0)
        while(r.angle > angle_res):
                time.sleep(time_res)

        print "starting..."

        start_time = time.time()
        r.set_angle(180)

        while(abs(r.angle-180) > angle_res):
                time.sleep(time_res)

        print("took %ss" % (time.time()-start_time))

def main():
        r = RotorGS("COM7")

        # rotate to 110 degrees
        r.set_angle(180)
        #time.sleep(25)


if __name__ == "__main__":
        setup_default_logging()
        main()
