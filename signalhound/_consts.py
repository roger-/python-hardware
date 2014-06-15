class SignalHoundError(Exception):
    pass

class SignalHoundNotFound(SignalHoundError):
    pass

class PacketHeaderNotFound(SignalHoundError):
    pass

class WriteFailed(SignalHoundError):
    pass

class WrongNumRead(SignalHoundError):
    pass

class ReadTimeout(SignalHoundError):
    pass

class DeviceNotLoaded(SignalHoundError):
    pass

class MissingData(SignalHoundError):
    pass

class ExtraData(SignalHoundError):
    pass

class OutOfRange(SignalHoundError):
    pass

class NoExtRef(SignalHoundError):
    pass

ERROR_CODES = {100:SignalHoundNotFound,
               101:PacketHeaderNotFound,
               102:WriteFailed,
               103:WrongNumRead,
               104:ReadTimeout,
               105:DeviceNotLoaded,
               106:MissingData,
               107:ExtraData,
               200:OutOfRange,
               201:NoExtRef}

SHAPI_Initialize = '?SHAPI_Initialize@@YAHXZ'
SHAPI_InitializeEx = '?SHAPI_InitializeEx@@YAHPAE@Z'
SHAPI_CopyCalTable = '?SHAPI_CopyCalTable@@YAHPAE@Z'
SHAPI_Configure = '?SHAPI_Configure@@YAHNHHHHH@Z'
SHAPI_ConfigureFast = '?SHAPI_ConfigureFast@@YAHNHHHHH@Z'
SHAPI_GetSlowSweep = '?SHAPI_GetSlowSweep@@YAHPANNNAAHHHH@Z'
SHAPI_GetFastSweep = '?SHAPI_GetFastSweep@@YAHPANNNAAHHH@Z'
SHAPI_GetLastChannelFreq = '?SHAPI_GetLastChannelFreq@@YANXZ'
SHAPI_CyclePort = '?SHAPI_CyclePort@@YAHXZ'
SHAPI_GetLastChannelFreq = '?SHAPI_GetLastChannelFreq@@YANXZ'
SHAPI_GetLastChannelPower = '?SHAPI_GetLastChannelPower@@YANXZ'
SHAPI_GetRBW = '?SHAPI_GetRBW@@YANHH@Z'
SHAPI_GetSlowSweepCount = '?SHAPI_GetSlowSweepCount@@YAHNNH@Z'
SHAPI_GetFastSweepCount = '?SHAPI_GetFastSweepCount@@YAHNNH@Z'
SHAPI_SelectExt10MHz = '?SHAPI_SelectExt10MHz@@YAHXZ'
SHAPI_Authenticate = '?SHAPI_Authenticate@@YAHH@Z'
SHAPI_GetIQDataPacket = '?SHAPI_GetIQDataPacket@@YAHPAH0AANH@Z'
SHAPI_StartStreamingData = '?SHAPI_StartStreamingData@@YAHH@Z'
SHAPI_StopStreamingData = '?SHAPI_StopStreamingData@@YAHH@Z'
SHAPI_GetStreamingPacket = '?SHAPI_GetStreamingPacket@@YAHPAH0H@Z'
SHAPI_SetupLO = '?SHAPI_SetupLO@@YAHAANHH@Z'
