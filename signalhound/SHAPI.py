import ctypes
from ctypes import CFUNCTYPE, byref, pointer, CFUNCTYPE
from _consts import *

SHAPI = ctypes.WinDLL('SH_API')

def errcheck(result, func, args):
    if result:
        if result in ERROR_CODES:
            raise ERROR_CODES[result]
        else:
            raise SignalHoundError('unknown error code %d' % result)

    return args

#######################
# int SHAPI_Initialize()
prototype = CFUNCTYPE(ctypes.c_int)
Initialize = prototype((SHAPI_Initialize, SHAPI))
Initialize.errcheck = errcheck
#######################

#######################
# int SHAPI_InitializeEx(unsigned char * p4KTable)
prototype = CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte))
paramflags = (1, 'p4KTable'),
InitializeEx = prototype((SHAPI_InitializeEx, SHAPI), paramflags)
InitializeEx.errcheck = errcheck

'''def InitializeEx(table):
    BUFF_SIZE = (4*1024)
    c_table = (ctypes.c_ubyte * BUFF_SIZE)(*table)

    _InitializeEx(c_table)'''

#######################

#######################
# int SHAPI_CopyCalTable (unsigned char * p4KTable)
prototype = CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte*(4*1024)))
paramflags = (2, 'p4KTable'),
CopyCalTable = prototype((SHAPI_CopyCalTable, SHAPI), paramflags)
CopyCalTable.errcheck = errcheck

'''def CopyCalTable():
    BUFF_SIZE =
    buff = (ctypes.c_ubyte * BUFF_SIZE)()

    _CopyCalTable(buff)

    return buff'''

#######################

#######################
# int SHAPI_Configure(double attenVal=10.0, int mixerBand=1, int sensitivity=0,
#                     int decimation=1, int IF_Path=0, int ADC_clock=0)
# int SHAPI_ConfigureFast(double attenVal=10.0, int mixerBand=1, int sensitivity=0,
#                     int decimation=1, int IF_Path=0, int ADC_clock=0)
prototype = CFUNCTYPE(ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_int,
                      ctypes.c_int, ctypes.c_int, ctypes.c_int)
paramflags = (1, "attenVal", 10.0), (1, "mixerBand", 1), (1, "sensitivity", 0),\
             (1, "decimation", 1), (1, "IF_Path", 0), (1, "ADC_clock", 0)
Configure = prototype((SHAPI_Configure, SHAPI), paramflags)
Configure.errcheck = errcheck
ConfigureFast = prototype((SHAPI_ConfigureFast, SHAPI), paramflags)
ConfigureFast.errcheck = errcheck
#######################

#######################
# int SHAPI_GetSlowSweep(double * dBArray, double startFreq, double stopFreq,
#                        int &returnCount, int FFTSize=1024, int avgCount=16,
#                        int imageHandling=0)
prototype = CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_double),
                      ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_int),
                      ctypes.c_int, ctypes.c_int, ctypes.c_int)
paramflags = (1, "dBArray"), (1, "startFreq"), (1, "stopFreq"),\
             (2, "returnCount"), (1, "FFTSize", 1024), (1, "avgCount", 16),\
             (1, "imageHandling", 0)
_GetSlowSweep = prototype((SHAPI_GetSlowSweep, SHAPI), paramflags)
_GetSlowSweep.errcheck = errcheck

def GetSlowSweep(startFreq, stopFreq, buff_size, FFTSize=1024, avgCount=16, imageHandling=0):
    buff = (ctypes.c_double * buff_size)()
    #returnCount = ctypes.c_int()

    returnCount = _GetSlowSweep(buff, startFreq, stopFreq, FFTSize,
                  avgCount, imageHandling)

    return returnCount, buff
#######################

#######################
# int SHAPI_GetFastSweep(double * dBArray, double startFreq, double stopFreq, int
#                        &returnCount, int FFTSize=16, int imageHandling=0)
prototype = CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_double),
                      ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_int),
                      ctypes.c_int, ctypes.c_int)
paramflags = (1, "dBArray"), (1, "startFreq"), (1, "stopFreq"),\
             (2, "returnCount"), (1, "FFTSize", 16), (1, "imageHandling", 0)
_GetFastSweep = prototype((SHAPI_GetFastSweep, SHAPI), paramflags)
_GetFastSweep.errcheck = errcheck

def GetFastSweep(startFreq, stopFreq, buff_size, FFTSize=16, imageHandling=0):
    buff = (ctypes.c_double * buff_size)()

    returnCount = _GetFastSweep(buff, startFreq, stopFreq, FFTSize, imageHandling)

    return returnCount, buff
#######################

#######################
# double SHAPI_GetLastChannelFreq()
prototype = CFUNCTYPE(ctypes.c_double)
GetLastChannelFreq = prototype((SHAPI_GetLastChannelFreq, SHAPI))
#######################

#######################
# double SHAPI_GetLastChannelPower()
prototype = CFUNCTYPE(ctypes.c_double)
GetLastChannelPower = prototype((SHAPI_GetLastChannelPower, SHAPI))
#######################

#######################
# double SHAPI_GetRBW(int FFTSize, int decimation)
prototype = CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.c_int)
paramflags = (1, 'FFTSize'), (1, 'decimation')
GetRBW = prototype((SHAPI_GetRBW, SHAPI), paramflags)
#######################

#######################
# int SHAPI_GetSlowSweepCount(double startFreq, double stopFreq, int FFTSize)
# int SHAPI_GetFastSweepCount(double startFreq, double stopFreq, int FFTSize);
prototype = CFUNCTYPE(ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_int)
paramflags = (1, 'startFreq'), (1, 'stopFreq'), (1, 'FFTSize')
GetFastSweepCount = prototype((SHAPI_GetFastSweepCount, SHAPI), paramflags)
GetSlowSweepCount = prototype((SHAPI_GetSlowSweepCount, SHAPI), paramflags)
#######################

#######################
# int SHAPI_CyclePort()
prototype = CFUNCTYPE(ctypes.c_int)
CyclePort = prototype((SHAPI_CyclePort, SHAPI))
CyclePort.errcheck = errcheck
#######################

#######################
# int SHAPI_SelectExt10MHz()
prototype = CFUNCTYPE(ctypes.c_int)
SelectExt10MHz = prototype((SHAPI_SelectExt10MHz, SHAPI))
SelectExt10MHz.errcheck = errcheck
#######################

#######################
# int SHAPI_Authenticate(int vendorcode=0)
prototype = CFUNCTYPE(ctypes.c_int, ctypes.c_int)
paramflags = (1, 'vendorcode', 0),
Authenticate = prototype((SHAPI_Authenticate, SHAPI), paramflags)
#######################

#######################
# int SHAPI_SetupLO(double &centerFreq, int mixMode=1)
#######################

#######################
# int SHAPI_GetIQDataPacket (int * pIData, int * pQData, double &centerFreq, int size)
prototype = CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int),
                      ctypes.POINTER(ctypes.c_double), ctypes.c_int)
paramflags = (1, "pIData"), (1, "pQData"), (3, "centerFreq"),\
             (1, "size")
_GetIQDataPacket = prototype((SHAPI_GetIQDataPacket, SHAPI), paramflags)
_GetIQDataPacket.errcheck = errcheck

def GetIQDataPacket(center_freq, buff_size):
    i_buff = (ctypes.c_int * buff_size)()
    q_buff = (ctypes.c_int * buff_size)()

    cf = ctypes.c_double(center_freq)

    _GetIQDataPacket(i_buff, q_buff, byref(cf), buff_size)

    return cf.value, i_buff, q_buff
#######################

#######################
# int SHAPI_StartStreamingData()
prototype = CFUNCTYPE(ctypes.c_int)
StartStreamingData = prototype((SHAPI_StartStreamingData, SHAPI))
StartStreamingData.errcheck = errcheck
#######################

#######################
# int SHAPI_StopStreamingData()
prototype = CFUNCTYPE(ctypes.c_int)
StopStreamingData = prototype((SHAPI_StopStreamingData, SHAPI))
StopStreamingData.errcheck = errcheck
#######################

#######################
# int SHAPI_GetStreamingPacket(int *bufI, int *bufQ)
prototype = CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte*(4*1024)), ctypes.POINTER(ctypes.c_ubyte*(4*1024)))
paramflags = (2, 'bufI'), (2, 'bufQ')
GetStreamingPacket = prototype((SHAPI_GetStreamingPacket, SHAPI), paramflags)
GetStreamingPacket.errcheck = errcheck
#######################

#######################
# int SHAPI_SetupLO(double &centerFreq, int mixMode=1)
prototype = CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.c_int)
paramflags = (1, 'centerFreq'), (1, 'mixMode', 1)
_SetupLO = prototype((SHAPI_SetupLO, SHAPI), paramflags)
_SetupLO.errcheck = errcheck

def SetupLO(center_freq, mixMode=1):
    cf = ctypes.c_double(center_freq)

    _SetupLO(byref(cf), mixMode)

    return cf.value
#######################

def main():
    import time

    Initialize()
    print('done init')

    ConfigureFast(mixerBand=1)
    print('done config')

    return

    cf = SetupLO(400000)

    print cf, cf.value




    n = GetFastSweepCount(700e6, 710e6, 256)
    print('done sweep count')
    print(n)

    c, x = GetFastSweep(700e6, 710e6, n, FFTSize=16, imageHandling=0)
    print('done sweep ')

    print(x[0:100])
    print(c)




if __name__ == '__main__':
    main()