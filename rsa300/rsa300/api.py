from ctypes import *
from ctypes.util import find_library


def load_library():
    LIBRARY_FILENAME = 'RSA300API.dll'

    lib_path = find_library(LIBRARY_FILENAME)

    try:
        lib = WinDLL(LIBRARY_FILENAME)
    except:
        raise ImportError('could not locate/load library')

    return lib

def error_check(result, func, arguments):
    NO_ERROR = 0

    if result == NO_ERROR:
        return

    error_str = GetErrorString(result)

    raise Exception('failed with error: ' + error_str)

_libs = [load_library()]


######################################################
# Following generated with ctypesgen (and hand edited)
######################################################

enum_anon_2 = c_int # RSA300API.h: 76

noError = 0 # RSA300API.h: 76

errorNotConnected = 1 # RSA300API.h: 76

errorTimeout = 2 # RSA300API.h: 76

errorTransfer = 3 # RSA300API.h: 76

errorFileOpen = 4 # RSA300API.h: 76

errorParameter = 5 # RSA300API.h: 76

errorDataNotReady = 6 # RSA300API.h: 76

errorInvalidCalibConstantFileFormat = 7 # RSA300API.h: 76

errorMismatchCalibConstantsSize = 8 # RSA300API.h: 76

errorFailed = 9 # RSA300API.h: 76

errorCRC = 10 # RSA300API.h: 76

errorWriteCalConfigHeader = 11 # RSA300API.h: 76

errorWriteCalConfigData = 12 # RSA300API.h: 76

errorReadCalConfigHeader = 13 # RSA300API.h: 76

errorReadCalConfigData = 14 # RSA300API.h: 76

errorEraseCalConfig = 15 # RSA300API.h: 76

errorCalConfigFileSize = 16 # RSA300API.h: 76

errorChangeToFlashMode = 17 # RSA300API.h: 76

errorChangeToRunMode = 18 # RSA300API.h: 76

errorIncompatibleFirmware = 19 # RSA300API.h: 76

errorBootLoaderNotRunning = 20 # RSA300API.h: 76

errorStreamADCToDiskFileOpen = 21 # RSA300API.h: 76

errorStreamADCToDiskAlreadyStreaming = 22 # RSA300API.h: 76

errorStreamADCToDiskBadPath = 23 # RSA300API.h: 76

errorStreamADCToDiskThreadFailure = 24 # RSA300API.h: 76

errorRebootFailure = 25 # RSA300API.h: 76

errorLOLockFailure = 26 # RSA300API.h: 76

errorPOSTFailureFPGALoad = 27 # RSA300API.h: 76

errorPOSTFailureHiPower = 28 # RSA300API.h: 76

errorPOSTFailureI2C = 29 # RSA300API.h: 76

errorPOSTFailureGPIF = 30 # RSA300API.h: 76

errorPOSTFailureUsbSpeed = 31 # RSA300API.h: 76

errorDSPLError = 32 # RSA300API.h: 76

errorDisconnectedDeviceRemoved = 33 # RSA300API.h: 76

errorDisconnectedDeviceNodeChangedAndRemoved = 34 # RSA300API.h: 76

errorDisconnectedTimeoutWaitingForADcData = 35 # RSA300API.h: 76

errorDisconnectedIOBeginTransfer = 36 # RSA300API.h: 76

errorOperationNotSupportedInSimMode = 37 # RSA300API.h: 76

errorStreamedFileInvalidHeader = 38 # RSA300API.h: 76

errorStreamedFileOpenFailure = 39 # RSA300API.h: 76

errorStreamingInvalidParameters = 40 # RSA300API.h: 76

errorStreamingEOF = 41 # RSA300API.h: 76

errorParameterTraceLength = 42 # RSA300API.h: 76

errorMeasurementNotEnabled = 43 # RSA300API.h: 76

errorSpanIsLessThanRBW = 44 # RSA300API.h: 76

errorStreamingFastForwardTimeInvalid = 45 # RSA300API.h: 76

errorFrequencyOutOfRange = 46 # RSA300API.h: 76

errorDisconnectedIOFinishTransfer = 47 # RSA300API.h: 76

errorIQStreamInvalidFileDataType = 48 # RSA300API.h: 76

errorIQStreamFileOpenFailed = 49 # RSA300API.h: 76

errorBufferAllocFailed = 50 # RSA300API.h: 76

errorPlaceholder = 9999 # RSA300API.h: 76

notImplemented = (-1) # RSA300API.h: 76

ReturnStatus = enum_anon_2 # RSA300API.h: 76

# RSA300API.h: 82
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'i',
    'q',
]
struct_anon_3._fields_ = [
    ('i', c_float),
    ('q', c_float),
]

Cplx32 = struct_anon_3 # RSA300API.h: 82

# RSA300API.h: 87
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'i',
    'q',
]
struct_anon_4._fields_ = [
    ('i', c_int32),
    ('q', c_int32),
]

CplxInt32 = struct_anon_4 # RSA300API.h: 87

# RSA300API.h: 92
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    'i',
    'q',
]
struct_anon_5._fields_ = [
    ('i', c_int16),
    ('q', c_int16),
]

CplxInt16 = struct_anon_5 # RSA300API.h: 92

# RSA300API.h: 101
for _lib in _libs:
    if not hasattr(_lib, 'Search'):
        continue
    Search = _lib.Search
    Search.argtypes = [POINTER(c_long), POINTER(POINTER(c_wchar)), POINTER(c_int)]
    Search.restype = ReturnStatus
    Search.errcheck = error_check
    break

# RSA300API.h: 102
for _lib in _libs:
    if not hasattr(_lib, 'Connect'):
        continue
    Connect = _lib.Connect
    Connect.argtypes = [c_long]
    Connect.restype = ReturnStatus
    Connect.errcheck = error_check
    break

# RSA300API.h: 103
for _lib in _libs:
    if not hasattr(_lib, 'ResetDevice'):
        continue
    ResetDevice = _lib.ResetDevice
    ResetDevice.argtypes = [c_long]
    ResetDevice.restype = ReturnStatus
    ResetDevice.errcheck = error_check
    break

# RSA300API.h: 104
for _lib in _libs:
    if not hasattr(_lib, 'Disconnect'):
        continue
    Disconnect = _lib.Disconnect
    Disconnect.argtypes = []
    Disconnect.restype = ReturnStatus
    Disconnect.errcheck = error_check
    break

# RSA300API.h: 113
for _lib in _libs:
    if not hasattr(_lib, 'GetAPIVersion'):
        continue
    GetAPIVersion = _lib.GetAPIVersion
    GetAPIVersion.argtypes = [c_char_p]
    GetAPIVersion.restype = ReturnStatus
    GetAPIVersion.errcheck = error_check
    break

# RSA300API.h: 114
for _lib in _libs:
    if not hasattr(_lib, 'GetFirmwareVersion'):
        continue
    GetFirmwareVersion = _lib.GetFirmwareVersion
    GetFirmwareVersion.argtypes = [c_char_p]
    GetFirmwareVersion.restype = ReturnStatus
    GetFirmwareVersion.errcheck = error_check
    break

# RSA300API.h: 115
for _lib in _libs:
    if not hasattr(_lib, 'GetFPGAVersion'):
        continue
    GetFPGAVersion = _lib.GetFPGAVersion
    GetFPGAVersion.argtypes = [c_char_p]
    GetFPGAVersion.restype = ReturnStatus
    GetFPGAVersion.errcheck = error_check
    break

# RSA300API.h: 116
for _lib in _libs:
    if not hasattr(_lib, 'GetHWVersion'):
        continue
    GetHWVersion = _lib.GetHWVersion
    GetHWVersion.argtypes = [c_char_p]
    GetHWVersion.restype = ReturnStatus
    GetHWVersion.errcheck = error_check
    break

# RSA300API.h: 117
for _lib in _libs:
    if not hasattr(_lib, 'GetDeviceSerialNumber'):
        continue
    GetDeviceSerialNumber = _lib.GetDeviceSerialNumber
    GetDeviceSerialNumber.argtypes = [c_char_p]
    GetDeviceSerialNumber.restype = ReturnStatus
    GetDeviceSerialNumber.errcheck = error_check
    break

# RSA300API.h: 118
for _lib in _libs:
    if not hasattr(_lib, 'GetDeviceNomenclature'):
        continue
    GetDeviceNomenclature = _lib.GetDeviceNomenclature
    GetDeviceNomenclature.argtypes = [c_char_p]
    GetDeviceNomenclature.restype = ReturnStatus
    GetDeviceNomenclature.errcheck = error_check
    break

# RSA300API.h: 120
for _lib in _libs:
    if not hasattr(_lib, 'GetErrorString'):
        continue
    GetErrorString = _lib.GetErrorString
    GetErrorString.argtypes = [ReturnStatus]
    GetErrorString.restype = c_char_p
    break

# RSA300API.h: 121
for _lib in _libs:
    if not hasattr(_lib, 'GetCalibConstantFilesVersion'):
        continue
    GetCalibConstantFilesVersion = _lib.GetCalibConstantFilesVersion
    GetCalibConstantFilesVersion.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), POINTER(c_int)]
    GetCalibConstantFilesVersion.restype = ReturnStatus
    GetCalibConstantFilesVersion.errcheck = error_check
    break

enum_anon_6 = c_int # RSA300API.h: 134

stopped = 0 # RSA300API.h: 134

running = 1 # RSA300API.h: 134

RunMode = enum_anon_6 # RSA300API.h: 134

# RSA300API.h: 136
for _lib in _libs:
    if not hasattr(_lib, 'Run'):
        continue
    Run = _lib.Run
    Run.argtypes = []
    Run.restype = ReturnStatus
    Run.errcheck = error_check
    break

# RSA300API.h: 137
for _lib in _libs:
    if not hasattr(_lib, 'PrepareForRun'):
        continue
    PrepareForRun = _lib.PrepareForRun
    PrepareForRun.argtypes = []
    PrepareForRun.restype = ReturnStatus
    PrepareForRun.errcheck = error_check
    break

# RSA300API.h: 138
for _lib in _libs:
    if not hasattr(_lib, 'StartFrameTransfer'):
        continue
    StartFrameTransfer = _lib.StartFrameTransfer
    StartFrameTransfer.argtypes = []
    StartFrameTransfer.restype = ReturnStatus
    StartFrameTransfer.errcheck = error_check
    break

# RSA300API.h: 139
for _lib in _libs:
    if not hasattr(_lib, 'Stop'):
        continue
    Stop = _lib.Stop
    Stop.argtypes = []
    Stop.restype = ReturnStatus
    Stop.errcheck = error_check
    break

# RSA300API.h: 140
for _lib in _libs:
    if not hasattr(_lib, 'GetRunState'):
        continue
    GetRunState = _lib.GetRunState
    GetRunState.argtypes = [POINTER(RunMode)]
    GetRunState.restype = ReturnStatus
    GetRunState.errcheck = error_check
    break

# RSA300API.h: 141
for _lib in _libs:
    if not hasattr(_lib, 'Preset'):
        continue
    Preset = _lib.Preset
    Preset.argtypes = []
    Preset.restype = ReturnStatus
    Preset.errcheck = error_check
    break

# RSA300API.h: 143
for _lib in _libs:
    if not hasattr(_lib, 'SetReferenceLevel'):
        continue
    SetReferenceLevel = _lib.SetReferenceLevel
    SetReferenceLevel.argtypes = [c_double]
    SetReferenceLevel.restype = ReturnStatus
    SetReferenceLevel.errcheck = error_check
    break

# RSA300API.h: 144
for _lib in _libs:
    if not hasattr(_lib, 'GetReferenceLevel'):
        continue
    GetReferenceLevel = _lib.GetReferenceLevel
    GetReferenceLevel.argtypes = [POINTER(c_double)]
    GetReferenceLevel.restype = ReturnStatus
    GetReferenceLevel.errcheck = error_check
    break

# RSA300API.h: 145
for _lib in _libs:
    if not hasattr(_lib, 'SetCenterFreq'):
        continue
    SetCenterFreq = _lib.SetCenterFreq
    SetCenterFreq.argtypes = [c_double]
    SetCenterFreq.restype = ReturnStatus
    SetCenterFreq.errcheck = error_check
    break

# RSA300API.h: 146
for _lib in _libs:
    if not hasattr(_lib, 'GetCenterFreq'):
        continue
    GetCenterFreq = _lib.GetCenterFreq
    GetCenterFreq.argtypes = [POINTER(c_double)]
    GetCenterFreq.restype = ReturnStatus
    GetCenterFreq.errcheck = error_check
    break

# RSA300API.h: 147
for _lib in _libs:
    if not hasattr(_lib, 'GetTunedCenterFreq'):
        continue
    GetTunedCenterFreq = _lib.GetTunedCenterFreq
    GetTunedCenterFreq.argtypes = [POINTER(c_double)]
    GetTunedCenterFreq.restype = ReturnStatus
    GetTunedCenterFreq.errcheck = error_check
    break

# RSA300API.h: 148
for _lib in _libs:
    if not hasattr(_lib, 'SetIQBandwidth'):
        continue
    SetIQBandwidth = _lib.SetIQBandwidth
    SetIQBandwidth.argtypes = [c_double]
    SetIQBandwidth.restype = ReturnStatus
    SetIQBandwidth.errcheck = error_check
    break

# RSA300API.h: 149
for _lib in _libs:
    if not hasattr(_lib, 'GetIQBandwidth'):
        continue
    GetIQBandwidth = _lib.GetIQBandwidth
    GetIQBandwidth.argtypes = [POINTER(c_double)]
    GetIQBandwidth.restype = ReturnStatus
    GetIQBandwidth.errcheck = error_check
    break

# RSA300API.h: 150
for _lib in _libs:
    if not hasattr(_lib, 'GetIQSampleRate'):
        continue
    GetIQSampleRate = _lib.GetIQSampleRate
    GetIQSampleRate.argtypes = [POINTER(c_double)]
    GetIQSampleRate.restype = ReturnStatus
    GetIQSampleRate.errcheck = error_check
    break

# RSA300API.h: 151
for _lib in _libs:
    if not hasattr(_lib, 'SetIQRecordLength'):
        continue
    SetIQRecordLength = _lib.SetIQRecordLength
    SetIQRecordLength.argtypes = [c_long]
    SetIQRecordLength.restype = ReturnStatus
    SetIQRecordLength.errcheck = error_check
    break

# RSA300API.h: 152
for _lib in _libs:
    if not hasattr(_lib, 'GetIQRecordLength'):
        continue
    GetIQRecordLength = _lib.GetIQRecordLength
    GetIQRecordLength.argtypes = [POINTER(c_long)]
    GetIQRecordLength.restype = ReturnStatus
    GetIQRecordLength.errcheck = error_check
    break

# RSA300API.h: 154
for _lib in _libs:
    if not hasattr(_lib, 'SetExternalRefEnable'):
        continue
    SetExternalRefEnable = _lib.SetExternalRefEnable
    SetExternalRefEnable.argtypes = [c_bool]
    SetExternalRefEnable.restype = ReturnStatus
    SetExternalRefEnable.errcheck = error_check
    break

# RSA300API.h: 155
for _lib in _libs:
    if not hasattr(_lib, 'GetExternalRefEnable'):
        continue
    GetExternalRefEnable = _lib.GetExternalRefEnable
    GetExternalRefEnable.argtypes = [POINTER(c_bool)]
    GetExternalRefEnable.restype = ReturnStatus
    GetExternalRefEnable.errcheck = error_check
    break

# RSA300API.h: 157
for _lib in _libs:
    if not hasattr(_lib, 'GetMaxIQBandwidth'):
        continue
    GetMaxIQBandwidth = _lib.GetMaxIQBandwidth
    GetMaxIQBandwidth.argtypes = [POINTER(c_double)]
    GetMaxIQBandwidth.restype = ReturnStatus
    GetMaxIQBandwidth.errcheck = error_check
    break

# RSA300API.h: 158
for _lib in _libs:
    if not hasattr(_lib, 'GetMinIQBandwidth'):
        continue
    GetMinIQBandwidth = _lib.GetMinIQBandwidth
    GetMinIQBandwidth.argtypes = [POINTER(c_double)]
    GetMinIQBandwidth.restype = ReturnStatus
    GetMinIQBandwidth.errcheck = error_check
    break

# RSA300API.h: 159
for _lib in _libs:
    if not hasattr(_lib, 'GetMaxCenterFreq'):
        continue
    GetMaxCenterFreq = _lib.GetMaxCenterFreq
    GetMaxCenterFreq.argtypes = [POINTER(c_double)]
    GetMaxCenterFreq.restype = ReturnStatus
    GetMaxCenterFreq.errcheck = error_check
    break

# RSA300API.h: 160
for _lib in _libs:
    if not hasattr(_lib, 'GetMinCenterFreq'):
        continue
    GetMinCenterFreq = _lib.GetMinCenterFreq
    GetMinCenterFreq.argtypes = [POINTER(c_double)]
    GetMinCenterFreq.restype = ReturnStatus
    GetMinCenterFreq.errcheck = error_check
    break

# RSA300API.h: 161
for _lib in _libs:
    if not hasattr(_lib, 'GetMaxAcquisitionSamples'):
        continue
    GetMaxAcquisitionSamples = _lib.GetMaxAcquisitionSamples
    GetMaxAcquisitionSamples.argtypes = [POINTER(c_ulong)]
    GetMaxAcquisitionSamples.restype = ReturnStatus
    GetMaxAcquisitionSamples.errcheck = error_check
    break

enum_anon_7 = c_int # RSA300API.h: 173

freeRun = 0 # RSA300API.h: 173

triggered = 1 # RSA300API.h: 173

TriggerMode = enum_anon_7 # RSA300API.h: 173

enum_anon_8 = c_int # RSA300API.h: 179

TriggerSourceExternal = 0 # RSA300API.h: 179

TriggerSourceIFPowerLevel = 1 # RSA300API.h: 179

TriggerSource = enum_anon_8 # RSA300API.h: 179

enum_anon_9 = c_int # RSA300API.h: 186

TriggerTransitionLH = 1 # RSA300API.h: 186

TriggerTransitionHL = 2 # RSA300API.h: 186

TriggerTransitionEither = 3 # RSA300API.h: 186

TriggerTransition = enum_anon_9 # RSA300API.h: 186

# RSA300API.h: 188
for _lib in _libs:
    if not hasattr(_lib, 'ForceTrigger'):
        continue
    ForceTrigger = _lib.ForceTrigger
    ForceTrigger.argtypes = []
    ForceTrigger.restype = ReturnStatus
    ForceTrigger.errcheck = error_check
    break

# RSA300API.h: 189
for _lib in _libs:
    if not hasattr(_lib, 'SetTriggerPositionPercent'):
        continue
    SetTriggerPositionPercent = _lib.SetTriggerPositionPercent
    SetTriggerPositionPercent.argtypes = [c_double]
    SetTriggerPositionPercent.restype = ReturnStatus
    SetTriggerPositionPercent.errcheck = error_check
    break

# RSA300API.h: 190
for _lib in _libs:
    if not hasattr(_lib, 'GetTriggerPositionPercent'):
        continue
    GetTriggerPositionPercent = _lib.GetTriggerPositionPercent
    GetTriggerPositionPercent.argtypes = [POINTER(c_double)]
    GetTriggerPositionPercent.restype = ReturnStatus
    GetTriggerPositionPercent.errcheck = error_check
    break

# RSA300API.h: 191
for _lib in _libs:
    if not hasattr(_lib, 'SetTriggerMode'):
        continue
    SetTriggerMode = _lib.SetTriggerMode
    SetTriggerMode.argtypes = [TriggerMode]
    SetTriggerMode.restype = ReturnStatus
    SetTriggerMode.errcheck = error_check
    break

# RSA300API.h: 192
for _lib in _libs:
    if not hasattr(_lib, 'GetTriggerMode'):
        continue
    GetTriggerMode = _lib.GetTriggerMode
    GetTriggerMode.argtypes = [POINTER(TriggerMode)]
    GetTriggerMode.restype = ReturnStatus
    GetTriggerMode.errcheck = error_check
    break

# RSA300API.h: 193
for _lib in _libs:
    if not hasattr(_lib, 'SetTriggerTransition'):
        continue
    SetTriggerTransition = _lib.SetTriggerTransition
    SetTriggerTransition.argtypes = [TriggerTransition]
    SetTriggerTransition.restype = ReturnStatus
    SetTriggerTransition.errcheck = error_check
    break

# RSA300API.h: 194
for _lib in _libs:
    if not hasattr(_lib, 'GetTriggerTransition'):
        continue
    GetTriggerTransition = _lib.GetTriggerTransition
    GetTriggerTransition.argtypes = [POINTER(TriggerTransition)]
    GetTriggerTransition.restype = ReturnStatus
    GetTriggerTransition.errcheck = error_check
    break

# RSA300API.h: 195
for _lib in _libs:
    if not hasattr(_lib, 'SetTriggerSource'):
        continue
    SetTriggerSource = _lib.SetTriggerSource
    SetTriggerSource.argtypes = [TriggerSource]
    SetTriggerSource.restype = ReturnStatus
    SetTriggerSource.errcheck = error_check
    break

# RSA300API.h: 196
for _lib in _libs:
    if not hasattr(_lib, 'GetTriggerSource'):
        continue
    GetTriggerSource = _lib.GetTriggerSource
    GetTriggerSource.argtypes = [POINTER(TriggerSource)]
    GetTriggerSource.restype = ReturnStatus
    GetTriggerSource.errcheck = error_check
    break

# RSA300API.h: 197
for _lib in _libs:
    if not hasattr(_lib, 'SetIFPowerTriggerLevel'):
        continue
    SetIFPowerTriggerLevel = _lib.SetIFPowerTriggerLevel
    SetIFPowerTriggerLevel.argtypes = [c_double]
    SetIFPowerTriggerLevel.restype = ReturnStatus
    SetIFPowerTriggerLevel.errcheck = error_check
    break

# RSA300API.h: 198
for _lib in _libs:
    if not hasattr(_lib, 'GetIFPowerTriggerLevel'):
        continue
    GetIFPowerTriggerLevel = _lib.GetIFPowerTriggerLevel
    GetIFPowerTriggerLevel.argtypes = [POINTER(c_double)]
    GetIFPowerTriggerLevel.restype = ReturnStatus
    GetIFPowerTriggerLevel.errcheck = error_check
    break

enum_anon_10 = c_int # RSA300API.h: 210

StreamingModeRaw = 0 # RSA300API.h: 210

StreamingModeFramed = (StreamingModeRaw + 1) # RSA300API.h: 210

StreamingMode = enum_anon_10 # RSA300API.h: 210

# RSA300API.h: 212
for _lib in _libs:
    if not hasattr(_lib, 'SetStreamADCToDiskEnabled'):
        continue
    SetStreamADCToDiskEnabled = _lib.SetStreamADCToDiskEnabled
    SetStreamADCToDiskEnabled.argtypes = [c_bool]
    SetStreamADCToDiskEnabled.restype = ReturnStatus
    SetStreamADCToDiskEnabled.errcheck = error_check
    break

# RSA300API.h: 213
for _lib in _libs:
    if not hasattr(_lib, 'SetStreamADCToDiskPath'):
        continue
    SetStreamADCToDiskPath = _lib.SetStreamADCToDiskPath
    SetStreamADCToDiskPath.argtypes = [c_char_p]
    SetStreamADCToDiskPath.restype = ReturnStatus
    SetStreamADCToDiskPath.errcheck = error_check
    break

# RSA300API.h: 214
for _lib in _libs:
    if not hasattr(_lib, 'SetStreamADCToDiskFilenameBase'):
        continue
    SetStreamADCToDiskFilenameBase = _lib.SetStreamADCToDiskFilenameBase
    SetStreamADCToDiskFilenameBase.argtypes = [c_char_p]
    SetStreamADCToDiskFilenameBase.restype = ReturnStatus
    SetStreamADCToDiskFilenameBase.errcheck = error_check
    break

# RSA300API.h: 215
for _lib in _libs:
    if not hasattr(_lib, 'SetStreamADCToDiskMaxTime'):
        continue
    SetStreamADCToDiskMaxTime = _lib.SetStreamADCToDiskMaxTime
    SetStreamADCToDiskMaxTime.argtypes = [c_long]
    SetStreamADCToDiskMaxTime.restype = ReturnStatus
    SetStreamADCToDiskMaxTime.errcheck = error_check
    break

# RSA300API.h: 216
for _lib in _libs:
    if not hasattr(_lib, 'SetStreamADCToDiskMode'):
        continue
    SetStreamADCToDiskMode = _lib.SetStreamADCToDiskMode
    SetStreamADCToDiskMode.argtypes = [StreamingMode]
    SetStreamADCToDiskMode.restype = ReturnStatus
    SetStreamADCToDiskMode.errcheck = error_check
    break

# RSA300API.h: 217
for _lib in _libs:
    if not hasattr(_lib, 'SetStreamADCToDiskMaxFileCount'):
        continue
    SetStreamADCToDiskMaxFileCount = _lib.SetStreamADCToDiskMaxFileCount
    SetStreamADCToDiskMaxFileCount.argtypes = [c_int]
    SetStreamADCToDiskMaxFileCount.restype = ReturnStatus
    SetStreamADCToDiskMaxFileCount.errcheck = error_check
    break

# RSA300API.h: 218
for _lib in _libs:
    if not hasattr(_lib, 'GetStreamADCToDiskActive'):
        continue
    GetStreamADCToDiskActive = _lib.GetStreamADCToDiskActive
    GetStreamADCToDiskActive.argtypes = [POINTER(c_bool)]
    GetStreamADCToDiskActive.restype = ReturnStatus
    GetStreamADCToDiskActive.errcheck = error_check
    break

# RSA300API.h: 229
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_SetAcqBandwidth'):
        continue
    IQSTREAM_SetAcqBandwidth = _lib.IQSTREAM_SetAcqBandwidth
    IQSTREAM_SetAcqBandwidth.argtypes = [c_double]
    IQSTREAM_SetAcqBandwidth.restype = ReturnStatus
    IQSTREAM_SetAcqBandwidth.errcheck = error_check
    break

# RSA300API.h: 230
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_GetAcqParameters'):
        continue
    IQSTREAM_GetAcqParameters = _lib.IQSTREAM_GetAcqParameters
    IQSTREAM_GetAcqParameters.argtypes = [POINTER(c_double), POINTER(c_double)]
    IQSTREAM_GetAcqParameters.restype = ReturnStatus
    IQSTREAM_GetAcqParameters.errcheck = error_check
    break

enum_anon_11 = c_int # RSA300API.h: 232

IQSOD_CLIENT = 0 # RSA300API.h: 232

IQSOD_FILE_TIQ = (IQSOD_CLIENT + 1) # RSA300API.h: 232

IQSOD_FILE_SIQ = (IQSOD_FILE_TIQ + 1) # RSA300API.h: 232

IQSOD_FILE_SIQ_SPLIT = (IQSOD_FILE_SIQ + 1) # RSA300API.h: 232

IQSOUTDEST = enum_anon_11 # RSA300API.h: 232

enum_anon_12 = c_int # RSA300API.h: 233

IQSODT_SINGLE = 0 # RSA300API.h: 233

IQSODT_INT32 = (IQSODT_SINGLE + 1) # RSA300API.h: 233

IQSODT_INT16 = (IQSODT_INT32 + 1) # RSA300API.h: 233

IQSOUTDTYPE = enum_anon_12 # RSA300API.h: 233

# RSA300API.h: 234
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_SetOutputConfiguration'):
        continue
    IQSTREAM_SetOutputConfiguration = _lib.IQSTREAM_SetOutputConfiguration
    IQSTREAM_SetOutputConfiguration.argtypes = [IQSOUTDEST, IQSOUTDTYPE]
    IQSTREAM_SetOutputConfiguration.restype = ReturnStatus
    IQSTREAM_SetOutputConfiguration.errcheck = error_check
    break

# RSA300API.h: 236
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_SetIQDataBufferSize'):
        continue
    IQSTREAM_SetIQDataBufferSize = _lib.IQSTREAM_SetIQDataBufferSize
    IQSTREAM_SetIQDataBufferSize.argtypes = [c_int]
    IQSTREAM_SetIQDataBufferSize.restype = ReturnStatus
    IQSTREAM_SetIQDataBufferSize.errcheck = error_check
    break

# RSA300API.h: 237
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_GetIQDataBufferSize'):
        continue
    IQSTREAM_GetIQDataBufferSize = _lib.IQSTREAM_GetIQDataBufferSize
    IQSTREAM_GetIQDataBufferSize.argtypes = [POINTER(c_int)]
    IQSTREAM_GetIQDataBufferSize.restype = ReturnStatus
    IQSTREAM_GetIQDataBufferSize.errcheck = error_check
    break

# RSA300API.h: 239
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_SetDiskFilenameBaseW'):
        continue
    IQSTREAM_SetDiskFilenameBaseW = _lib.IQSTREAM_SetDiskFilenameBaseW
    IQSTREAM_SetDiskFilenameBaseW.argtypes = [POINTER(c_wchar)]
    IQSTREAM_SetDiskFilenameBaseW.restype = ReturnStatus
    IQSTREAM_SetDiskFilenameBaseW.errcheck = error_check
    break

# RSA300API.h: 240
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_SetDiskFilenameBase'):
        continue
    IQSTREAM_SetDiskFilenameBase = _lib.IQSTREAM_SetDiskFilenameBase
    IQSTREAM_SetDiskFilenameBase.argtypes = [c_char_p]
    IQSTREAM_SetDiskFilenameBase.restype = ReturnStatus
    IQSTREAM_SetDiskFilenameBase.errcheck = error_check
    break

enum_anon_13 = c_int # RSA300API.h: 241

IQSSDFN_SUFFIX_INCRINDEX_MIN = 0 # RSA300API.h: 241

IQSSDFN_SUFFIX_TIMESTAMP = (-1) # RSA300API.h: 241

IQSSDFN_SUFFIX_NONE = (-2) # RSA300API.h: 241

# RSA300API.h: 242
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_SetDiskFilenameSuffix'):
        continue
    IQSTREAM_SetDiskFilenameSuffix = _lib.IQSTREAM_SetDiskFilenameSuffix
    IQSTREAM_SetDiskFilenameSuffix.argtypes = [c_int]
    IQSTREAM_SetDiskFilenameSuffix.restype = ReturnStatus
    IQSTREAM_SetDiskFilenameSuffix.errcheck = error_check
    break

# RSA300API.h: 243
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_SetDiskFileLength'):
        continue
    IQSTREAM_SetDiskFileLength = _lib.IQSTREAM_SetDiskFileLength
    IQSTREAM_SetDiskFileLength.argtypes = [c_int]
    IQSTREAM_SetDiskFileLength.restype = ReturnStatus
    IQSTREAM_SetDiskFileLength.errcheck = error_check
    break

# RSA300API.h: 245
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_Start'):
        continue
    IQSTREAM_Start = _lib.IQSTREAM_Start
    IQSTREAM_Start.argtypes = []
    IQSTREAM_Start.restype = ReturnStatus
    IQSTREAM_Start.errcheck = error_check
    break

# RSA300API.h: 246
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_Stop'):
        continue
    IQSTREAM_Stop = _lib.IQSTREAM_Stop
    IQSTREAM_Stop.argtypes = []
    IQSTREAM_Stop.restype = ReturnStatus
    IQSTREAM_Stop.errcheck = error_check
    break

# RSA300API.h: 247
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_GetEnabled'):
        continue
    IQSTREAM_GetEnabled = _lib.IQSTREAM_GetEnabled
    IQSTREAM_GetEnabled.argtypes = [POINTER(c_bool)]
    IQSTREAM_GetEnabled.restype = ReturnStatus
    IQSTREAM_GetEnabled.errcheck = error_check
    break

enum_anon_14 = c_int # RSA300API.h: 249

IQSTRM_STATUS_OVERRANGE = (1 << 0) # RSA300API.h: 249

IQSTRM_STATUS_UNUSED1 = (1 << 1) # RSA300API.h: 249

IQSTRM_STATUS_IBUFF75PCT = (1 << 2) # RSA300API.h: 249

IQSTRM_STATUS_IBUFFOVFLOW = (1 << 3) # RSA300API.h: 249

IQSTRM_STATUS_OBUFF75PCT = (1 << 4) # RSA300API.h: 249

IQSTRM_STATUS_OBUFFOVFLOW = (1 << 5) # RSA300API.h: 249

IQSTRM_STATUS_NONSTICKY_SHIFT = 0 # RSA300API.h: 249

IQSTRM_STATUS_STICKY_SHIFT = 16 # RSA300API.h: 249

enum_anon_15 = c_int # RSA300API.h: 260

IQSTRM_MAXTRIGGERS = 100 # RSA300API.h: 260

# RSA300API.h: 268
class struct_anon_16(Structure):
    pass

struct_anon_16.__slots__ = [
    'timestamp',
    'triggerCount',
    'triggerIndices',
    'scaleFactor',
    'acqStatus',
]
struct_anon_16._fields_ = [
    ('timestamp', c_uint64),
    ('triggerCount', c_int),
    ('triggerIndices', POINTER(c_int)),
    ('scaleFactor', c_double),
    ('acqStatus', c_uint32),
]

IQSTRMIQINFO = struct_anon_16 # RSA300API.h: 268

# RSA300API.h: 270
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_GetIQData'):
        continue
    IQSTREAM_GetIQData = _lib.IQSTREAM_GetIQData
    IQSTREAM_GetIQData.argtypes = [POINTER(None), POINTER(c_int), POINTER(IQSTRMIQINFO)]
    IQSTREAM_GetIQData.restype = ReturnStatus
    IQSTREAM_GetIQData.errcheck = error_check
    break

# RSA300API.h: 272
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_GetDiskFileWriteStatus'):
        continue
    IQSTREAM_GetDiskFileWriteStatus = _lib.IQSTREAM_GetDiskFileWriteStatus
    IQSTREAM_GetDiskFileWriteStatus.argtypes = [POINTER(c_bool), POINTER(c_bool)]
    IQSTREAM_GetDiskFileWriteStatus.restype = ReturnStatus
    IQSTREAM_GetDiskFileWriteStatus.errcheck = error_check
    break

enum_anon_17 = c_int # RSA300API.h: 274

IQSTRM_FILENAME_DATA_IDX = 0 # RSA300API.h: 274

IQSTRM_FILENAME_HEADER_IDX = 1 # RSA300API.h: 274

# RSA300API.h: 283
class struct_anon_18(Structure):
    pass

struct_anon_18.__slots__ = [
    'numberSamples',
    'sample0Timestamp',
    'triggerSampleIndex',
    'triggerTimestamp',
    'acqStatus',
    'filenames',
]
struct_anon_18._fields_ = [
    ('numberSamples', c_uint64),
    ('sample0Timestamp', c_uint64),
    ('triggerSampleIndex', c_uint64),
    ('triggerTimestamp', c_uint64),
    ('acqStatus', c_uint32),
    ('filenames', POINTER(POINTER(c_wchar))),
]

IQSTRMFILEINFO = struct_anon_18 # RSA300API.h: 283

# RSA300API.h: 284
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_GetFileInfo'):
        continue
    IQSTREAM_GetFileInfo = _lib.IQSTREAM_GetFileInfo
    IQSTREAM_GetFileInfo.argtypes = [POINTER(IQSTRMFILEINFO)]
    IQSTREAM_GetFileInfo.restype = ReturnStatus
    IQSTREAM_GetFileInfo.errcheck = error_check
    break

# RSA300API.h: 286
for _lib in _libs:
    if not hasattr(_lib, 'IQSTREAM_ClearAcqStatus'):
        continue
    IQSTREAM_ClearAcqStatus = _lib.IQSTREAM_ClearAcqStatus
    IQSTREAM_ClearAcqStatus.argtypes = []
    IQSTREAM_ClearAcqStatus.restype = None
    break

# RSA300API.h: 293
for _lib in _libs:
    if not hasattr(_lib, 'REFTIME_GetTimestampRate'):
        continue
    REFTIME_GetTimestampRate = _lib.REFTIME_GetTimestampRate
    REFTIME_GetTimestampRate.argtypes = [POINTER(c_uint64)]
    REFTIME_GetTimestampRate.restype = ReturnStatus
    REFTIME_GetTimestampRate.errcheck = error_check
    break

# RSA300API.h: 297
for _lib in _libs:
    if not hasattr(_lib, 'REFTIME_GetIntervalSinceRefTimeSet'):
        continue
    REFTIME_GetIntervalSinceRefTimeSet = _lib.REFTIME_GetIntervalSinceRefTimeSet
    REFTIME_GetIntervalSinceRefTimeSet.argtypes = [POINTER(c_double)]
    REFTIME_GetIntervalSinceRefTimeSet.restype = ReturnStatus
    REFTIME_GetIntervalSinceRefTimeSet.errcheck = error_check
    break

# RSA300API.h: 311
class struct_anon_19(Structure):
    pass

struct_anon_19.__slots__ = [
    'acqDataStatus',
    'acquisitionTimestamp',
    'frameID',
    'trigger1Index',
    'trigger2Index',
    'timeSyncIndex',
]
struct_anon_19._fields_ = [
    ('acqDataStatus', c_uint16),
    ('acquisitionTimestamp', c_uint64),
    ('frameID', c_uint32),
    ('trigger1Index', c_uint16),
    ('trigger2Index', c_uint16),
    ('timeSyncIndex', c_uint16),
]

IQHeader = struct_anon_19 # RSA300API.h: 311

enum_anon_20 = c_int # RSA300API.h: 340

adcOverrange = 1 # RSA300API.h: 340

refFreqUnlock = 2 # RSA300API.h: 340

lo1Unlock = 4 # RSA300API.h: 340

lo2Unlock = 8 # RSA300API.h: 340

lowSupplyVoltage = 16 # RSA300API.h: 340

adcDataLost = 32 # RSA300API.h: 340

event1pps = 64 # RSA300API.h: 340

eventTrig1 = 128 # RSA300API.h: 340

eventTrig2 = 256 # RSA300API.h: 340

AcqDataStatus = enum_anon_20 # RSA300API.h: 340

# RSA300API.h: 341
for _lib in _libs:
    if not hasattr(_lib, 'GetIQHeader'):
        continue
    GetIQHeader = _lib.GetIQHeader
    GetIQHeader.argtypes = [POINTER(IQHeader)]
    GetIQHeader.restype = ReturnStatus
    GetIQHeader.errcheck = error_check
    break

# RSA300API.h: 342
for _lib in _libs:
    if not hasattr(_lib, 'GetIQData'):
        continue
    GetIQData = _lib.GetIQData
    GetIQData.argtypes = [POINTER(c_float), c_int, c_int]
    GetIQData.restype = ReturnStatus
    GetIQData.errcheck = error_check
    break

# RSA300API.h: 343
for _lib in _libs:
    if not hasattr(_lib, 'GetIQDataDeinterleaved'):
        continue
    GetIQDataDeinterleaved = _lib.GetIQDataDeinterleaved
    GetIQDataDeinterleaved.argtypes = [POINTER(c_float), POINTER(c_float), c_int, c_int]
    GetIQDataDeinterleaved.restype = ReturnStatus
    GetIQDataDeinterleaved.errcheck = error_check
    break

# RSA300API.h: 344
for _lib in _libs:
    if not hasattr(_lib, 'GetIQDataCplx'):
        continue
    GetIQDataCplx = _lib.GetIQDataCplx
    GetIQDataCplx.argtypes = [POINTER(Cplx32), c_int, c_int]
    GetIQDataCplx.restype = ReturnStatus
    GetIQDataCplx.errcheck = error_check
    break

# RSA300API.h: 345
for _lib in _libs:
    if not hasattr(_lib, 'WaitForIQDataReady'):
        continue
    WaitForIQDataReady = _lib.WaitForIQDataReady
    WaitForIQDataReady.argtypes = [c_int, POINTER(c_bool)]
    WaitForIQDataReady.restype = ReturnStatus
    WaitForIQDataReady.errcheck = error_check
    break

# RSA300API.h: 385
class struct_anon_21(Structure):
    pass

struct_anon_21.__slots__ = [
    'fftPerFrame',
    'fftCount',
    'frameCount',
    'timestamp',
    'acqDataStatus',
    'minSigDuration',
    'minSigDurOutOfRange',
    'spectrumBitmapWidth',
    'spectrumBitmapHeight',
    'spectrumBitmapSize',
    'spectrumTraceLength',
    'numSpectrumTraces',
    'spectrumEnabled',
    'spectrogramEnabled',
    'spectrumBitmap',
    'spectrumTraces',
    'sogramBitmapWidth',
    'sogramBitmapHeight',
    'sogramBitmapSize',
    'sogramBitmapNumValidLines',
    'sogramBitmap',
    'sogramBitmapTimestampArray',
    'sogramBitmapContainTriggerArray',
]
struct_anon_21._fields_ = [
    ('fftPerFrame', c_int32),
    ('fftCount', c_int64),
    ('frameCount', c_int64),
    ('timestamp', c_double),
    ('acqDataStatus', c_uint32),
    ('minSigDuration', c_double),
    ('minSigDurOutOfRange', c_bool),
    ('spectrumBitmapWidth', c_int32),
    ('spectrumBitmapHeight', c_int32),
    ('spectrumBitmapSize', c_int32),
    ('spectrumTraceLength', c_int32),
    ('numSpectrumTraces', c_int32),
    ('spectrumEnabled', c_bool),
    ('spectrogramEnabled', c_bool),
    ('spectrumBitmap', POINTER(c_float)),
    ('spectrumTraces', POINTER(POINTER(c_float))),
    ('sogramBitmapWidth', c_int32),
    ('sogramBitmapHeight', c_int32),
    ('sogramBitmapSize', c_int32),
    ('sogramBitmapNumValidLines', c_int32),
    ('sogramBitmap', POINTER(c_uint8)),
    ('sogramBitmapTimestampArray', POINTER(c_double)),
    ('sogramBitmapContainTriggerArray', POINTER(c_int16)),
]

DPX_FrameBuffer = struct_anon_21 # RSA300API.h: 385

# RSA300API.h: 393
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'bitmapWidth',
    'bitmapHeight',
    'sogramTraceLineTime',
    'sogramBitmapLineTime',
]
struct_anon_22._fields_ = [
    ('bitmapWidth', c_int32),
    ('bitmapHeight', c_int32),
    ('sogramTraceLineTime', c_double),
    ('sogramBitmapLineTime', c_double),
]

DPX_SogramSettingsStruct = struct_anon_22 # RSA300API.h: 393

# RSA300API.h: 404
class struct_anon_23(Structure):
    pass

struct_anon_23.__slots__ = [
    'enableSpectrum',
    'enableSpectrogram',
    'bitmapWidth',
    'bitmapHeight',
    'traceLength',
    'decayFactor',
    'actualRBW',
]
struct_anon_23._fields_ = [
    ('enableSpectrum', c_bool),
    ('enableSpectrogram', c_bool),
    ('bitmapWidth', c_int32),
    ('bitmapHeight', c_int32),
    ('traceLength', c_int32),
    ('decayFactor', c_float),
    ('actualRBW', c_double),
]

DPX_SettingsStruct = struct_anon_23 # RSA300API.h: 404

enum_anon_24 = c_int # RSA300API.h: 413

TraceTypeAverage = 0 # RSA300API.h: 413

TraceTypeMax = (TraceTypeAverage + 1) # RSA300API.h: 413

TraceTypeMaxHold = (TraceTypeMax + 1) # RSA300API.h: 413

TraceTypeMin = (TraceTypeMaxHold + 1) # RSA300API.h: 413

TraceTypeMinHold = (TraceTypeMin + 1) # RSA300API.h: 413

TraceType = enum_anon_24 # RSA300API.h: 413

enum_anon_25 = c_int # RSA300API.h: 421

VerticalUnit_dBm = 0 # RSA300API.h: 421

VerticalUnit_Watt = (VerticalUnit_dBm + 1) # RSA300API.h: 421

VerticalUnit_Volt = (VerticalUnit_Watt + 1) # RSA300API.h: 421

VerticalUnit_Amp = (VerticalUnit_Volt + 1) # RSA300API.h: 421

VerticalUnitType = enum_anon_25 # RSA300API.h: 421

# RSA300API.h: 423
for _lib in _libs:
    if not hasattr(_lib, 'GetDPXEnabled'):
        continue
    GetDPXEnabled = _lib.GetDPXEnabled
    GetDPXEnabled.argtypes = [POINTER(c_bool)]
    GetDPXEnabled.restype = ReturnStatus
    GetDPXEnabled.errcheck = error_check
    break

# RSA300API.h: 424
for _lib in _libs:
    if not hasattr(_lib, 'SetDPXEnabled'):
        continue
    SetDPXEnabled = _lib.SetDPXEnabled
    SetDPXEnabled.argtypes = [c_bool]
    SetDPXEnabled.restype = ReturnStatus
    SetDPXEnabled.errcheck = error_check
    break

# RSA300API.h: 426
for _lib in _libs:
    if not hasattr(_lib, 'DPX_SetParameters'):
        continue
    DPX_SetParameters = _lib.DPX_SetParameters
    DPX_SetParameters.argtypes = [c_double, c_double, c_int32, c_int32, VerticalUnitType, c_double, c_double, c_bool, c_double, c_bool]
    DPX_SetParameters.restype = ReturnStatus
    DPX_SetParameters.errcheck = error_check
    break

# RSA300API.h: 427
for _lib in _libs:
    if not hasattr(_lib, 'DPX_Configure'):
        continue
    DPX_Configure = _lib.DPX_Configure
    DPX_Configure.argtypes = [c_bool, c_bool]
    DPX_Configure.restype = ReturnStatus
    DPX_Configure.errcheck = error_check
    break

# RSA300API.h: 428
for _lib in _libs:
    if not hasattr(_lib, 'DPX_GetSettings'):
        continue
    DPX_GetSettings = _lib.DPX_GetSettings
    DPX_GetSettings.argtypes = [POINTER(DPX_SettingsStruct)]
    DPX_GetSettings.restype = ReturnStatus
    DPX_GetSettings.errcheck = error_check
    break

# RSA300API.h: 429
for _lib in _libs:
    if not hasattr(_lib, 'DPX_SetSpectrumTraceType'):
        continue
    DPX_SetSpectrumTraceType = _lib.DPX_SetSpectrumTraceType
    DPX_SetSpectrumTraceType.argtypes = [c_int32, TraceType]
    DPX_SetSpectrumTraceType.restype = ReturnStatus
    DPX_SetSpectrumTraceType.errcheck = error_check
    break

# RSA300API.h: 430
for _lib in _libs:
    if not hasattr(_lib, 'DPX_FindRBWRange'):
        continue
    DPX_FindRBWRange = _lib.DPX_FindRBWRange
    DPX_FindRBWRange.argtypes = [c_double, POINTER(c_double), POINTER(c_double)]
    DPX_FindRBWRange.restype = ReturnStatus
    DPX_FindRBWRange.errcheck = error_check
    break

# RSA300API.h: 431
for _lib in _libs:
    if not hasattr(_lib, 'DPX_ResetDPx'):
        continue
    DPX_ResetDPx = _lib.DPX_ResetDPx
    DPX_ResetDPx.argtypes = []
    DPX_ResetDPx.restype = ReturnStatus
    DPX_ResetDPx.errcheck = error_check
    break

# RSA300API.h: 433
for _lib in _libs:
    if not hasattr(_lib, 'DPX_GetFrameInfo'):
        continue
    DPX_GetFrameInfo = _lib.DPX_GetFrameInfo
    DPX_GetFrameInfo.argtypes = [POINTER(c_int64), POINTER(c_int64)]
    DPX_GetFrameInfo.restype = ReturnStatus
    DPX_GetFrameInfo.errcheck = error_check
    break

# RSA300API.h: 436
for _lib in _libs:
    if not hasattr(_lib, 'DPX_SetSogramParameters'):
        continue
    DPX_SetSogramParameters = _lib.DPX_SetSogramParameters
    DPX_SetSogramParameters.argtypes = [c_double, c_double, c_double, c_double]
    DPX_SetSogramParameters.restype = ReturnStatus
    DPX_SetSogramParameters.errcheck = error_check
    break

# RSA300API.h: 437
for _lib in _libs:
    if not hasattr(_lib, 'DPX_SetSogramTraceType'):
        continue
    DPX_SetSogramTraceType = _lib.DPX_SetSogramTraceType
    DPX_SetSogramTraceType.argtypes = [TraceType]
    DPX_SetSogramTraceType.restype = ReturnStatus
    DPX_SetSogramTraceType.errcheck = error_check
    break

# RSA300API.h: 438
for _lib in _libs:
    if not hasattr(_lib, 'DPX_GetSogramSettings'):
        continue
    DPX_GetSogramSettings = _lib.DPX_GetSogramSettings
    DPX_GetSogramSettings.argtypes = [POINTER(DPX_SogramSettingsStruct)]
    DPX_GetSogramSettings.restype = ReturnStatus
    DPX_GetSogramSettings.errcheck = error_check
    break

# RSA300API.h: 440
for _lib in _libs:
    if not hasattr(_lib, 'DPX_GetSogramHiResLineCountLatest'):
        continue
    DPX_GetSogramHiResLineCountLatest = _lib.DPX_GetSogramHiResLineCountLatest
    DPX_GetSogramHiResLineCountLatest.argtypes = [POINTER(c_int32)]
    DPX_GetSogramHiResLineCountLatest.restype = ReturnStatus
    DPX_GetSogramHiResLineCountLatest.errcheck = error_check
    break

# RSA300API.h: 441
for _lib in _libs:
    if not hasattr(_lib, 'DPX_GetSogramHiResLineTriggered'):
        continue
    DPX_GetSogramHiResLineTriggered = _lib.DPX_GetSogramHiResLineTriggered
    DPX_GetSogramHiResLineTriggered.argtypes = [POINTER(c_bool), c_int32]
    DPX_GetSogramHiResLineTriggered.restype = ReturnStatus
    DPX_GetSogramHiResLineTriggered.errcheck = error_check
    break

# RSA300API.h: 442
for _lib in _libs:
    if not hasattr(_lib, 'DPX_GetSogramHiResLineTimestamp'):
        continue
    DPX_GetSogramHiResLineTimestamp = _lib.DPX_GetSogramHiResLineTimestamp
    DPX_GetSogramHiResLineTimestamp.argtypes = [POINTER(c_double), c_int32]
    DPX_GetSogramHiResLineTimestamp.restype = ReturnStatus
    DPX_GetSogramHiResLineTimestamp.errcheck = error_check
    break

# RSA300API.h: 443
for _lib in _libs:
    if not hasattr(_lib, 'DPX_GetSogramHiResLine'):
        continue
    DPX_GetSogramHiResLine = _lib.DPX_GetSogramHiResLine
    DPX_GetSogramHiResLine.argtypes = [POINTER(c_int16), POINTER(c_int32), c_int32, POINTER(c_double), c_int32, c_int32]
    DPX_GetSogramHiResLine.restype = ReturnStatus
    DPX_GetSogramHiResLine.errcheck = error_check
    break

# RSA300API.h: 445
for _lib in _libs:
    if not hasattr(_lib, 'WaitForDPXDataReady'):
        continue
    WaitForDPXDataReady = _lib.WaitForDPXDataReady
    WaitForDPXDataReady.argtypes = [c_int, POINTER(c_bool)]
    WaitForDPXDataReady.restype = ReturnStatus
    WaitForDPXDataReady.errcheck = error_check
    break

# RSA300API.h: 448
for _lib in _libs:
    if not hasattr(_lib, 'DPX_GetFrameBuffer'):
        continue
    DPX_GetFrameBuffer = _lib.DPX_GetFrameBuffer
    DPX_GetFrameBuffer.argtypes = [POINTER(DPX_FrameBuffer)]
    DPX_GetFrameBuffer.restype = ReturnStatus
    DPX_GetFrameBuffer.errcheck = error_check
    break

# RSA300API.h: 451
for _lib in _libs:
    if not hasattr(_lib, 'DPX_FinishFrameBuffer'):
        continue
    DPX_FinishFrameBuffer = _lib.DPX_FinishFrameBuffer
    DPX_FinishFrameBuffer.argtypes = []
    DPX_FinishFrameBuffer.restype = ReturnStatus
    DPX_FinishFrameBuffer.errcheck = error_check
    break

# RSA300API.h: 452
for _lib in _libs:
    if not hasattr(_lib, 'DPX_IsFrameBufferAvailable'):
        continue
    DPX_IsFrameBufferAvailable = _lib.DPX_IsFrameBufferAvailable
    DPX_IsFrameBufferAvailable.argtypes = [POINTER(c_bool)]
    DPX_IsFrameBufferAvailable.restype = ReturnStatus
    DPX_IsFrameBufferAvailable.errcheck = error_check
    break

enum_anon_26 = c_int # RSA300API.h: 468

ADM_FM_8KHZ = 0 # RSA300API.h: 468

ADM_FM_13KHZ = (ADM_FM_8KHZ + 1) # RSA300API.h: 468

ADM_FM_75KHZ = (ADM_FM_13KHZ + 1) # RSA300API.h: 468

ADM_FM_200KHZ = (ADM_FM_75KHZ + 1) # RSA300API.h: 468

ADM_AM_8KHZ = (ADM_FM_200KHZ + 1) # RSA300API.h: 468

AudioDemodMode = enum_anon_26 # RSA300API.h: 468

# RSA300API.h: 471
for _lib in _libs:
    if not hasattr(_lib, 'AUDIO_StartAudio'):
        continue
    AUDIO_StartAudio = _lib.AUDIO_StartAudio
    AUDIO_StartAudio.argtypes = []
    AUDIO_StartAudio.restype = ReturnStatus
    AUDIO_StartAudio.errcheck = error_check
    break

# RSA300API.h: 473
for _lib in _libs:
    if not hasattr(_lib, 'AUDIO_StopAudio'):
        continue
    AUDIO_StopAudio = _lib.AUDIO_StopAudio
    AUDIO_StopAudio.argtypes = []
    AUDIO_StopAudio.restype = ReturnStatus
    AUDIO_StopAudio.errcheck = error_check
    break

# RSA300API.h: 475
for _lib in _libs:
    if not hasattr(_lib, 'AUDIO_Running'):
        continue
    AUDIO_Running = _lib.AUDIO_Running
    AUDIO_Running.argtypes = [POINTER(c_bool)]
    AUDIO_Running.restype = ReturnStatus
    AUDIO_Running.errcheck = error_check
    break

# RSA300API.h: 480
for _lib in _libs:
    if not hasattr(_lib, 'AUDIO_GetData'):
        continue
    AUDIO_GetData = _lib.AUDIO_GetData
    AUDIO_GetData.argtypes = [POINTER(c_int16), c_uint16, POINTER(c_uint16)]
    AUDIO_GetData.restype = ReturnStatus
    AUDIO_GetData.errcheck = error_check
    break

# RSA300API.h: 488
for _lib in _libs:
    if not hasattr(_lib, 'AUDIO_SetMode'):
        continue
    AUDIO_SetMode = _lib.AUDIO_SetMode
    AUDIO_SetMode.argtypes = [AudioDemodMode]
    AUDIO_SetMode.restype = ReturnStatus
    AUDIO_SetMode.errcheck = error_check
    break

# RSA300API.h: 489
for _lib in _libs:
    if not hasattr(_lib, 'AUDIO_GetMode'):
        continue
    AUDIO_GetMode = _lib.AUDIO_GetMode
    AUDIO_GetMode.argtypes = [POINTER(AudioDemodMode)]
    AUDIO_GetMode.restype = ReturnStatus
    AUDIO_GetMode.errcheck = error_check
    break

# RSA300API.h: 492
for _lib in _libs:
    if not hasattr(_lib, 'AUDIO_SetVolume'):
        continue
    AUDIO_SetVolume = _lib.AUDIO_SetVolume
    AUDIO_SetVolume.argtypes = [c_float]
    AUDIO_SetVolume.restype = ReturnStatus
    AUDIO_SetVolume.errcheck = error_check
    break

# RSA300API.h: 493
for _lib in _libs:
    if not hasattr(_lib, 'AUDIO_GetVolume'):
        continue
    AUDIO_GetVolume = _lib.AUDIO_GetVolume
    AUDIO_GetVolume.argtypes = [POINTER(c_float)]
    AUDIO_GetVolume.restype = ReturnStatus
    AUDIO_GetVolume.errcheck = error_check
    break

# RSA300API.h: 497
for _lib in _libs:
    if not hasattr(_lib, 'AUDIO_SetMute'):
        continue
    AUDIO_SetMute = _lib.AUDIO_SetMute
    AUDIO_SetMute.argtypes = [c_bool]
    AUDIO_SetMute.restype = ReturnStatus
    AUDIO_SetMute.errcheck = error_check
    break

# RSA300API.h: 498
for _lib in _libs:
    if not hasattr(_lib, 'AUDIO_GetMute'):
        continue
    AUDIO_GetMute = _lib.AUDIO_GetMute
    AUDIO_GetMute.argtypes = [POINTER(c_bool)]
    AUDIO_GetMute.restype = ReturnStatus
    AUDIO_GetMute.errcheck = error_check
    break

# RSA300API.h: 506
for _lib in _libs:
    if not hasattr(_lib, 'POST_QueryStatus'):
        continue
    POST_QueryStatus = _lib.POST_QueryStatus
    POST_QueryStatus.argtypes = []
    POST_QueryStatus.restype = ReturnStatus
    POST_QueryStatus.errcheck = error_check
    break

# RSA300API.h: 514
for _lib in _libs:
    if not hasattr(_lib, 'GetDeviceTemperature'):
        continue
    GetDeviceTemperature = _lib.GetDeviceTemperature
    GetDeviceTemperature.argtypes = []
    GetDeviceTemperature.restype = c_double
    break

# RSA300API.h: 515
for _lib in _libs:
    if not hasattr(_lib, 'RunAlignment'):
        continue
    RunAlignment = _lib.RunAlignment
    RunAlignment.argtypes = []
    RunAlignment.restype = ReturnStatus
    RunAlignment.errcheck = error_check
    break

# RSA300API.h: 516
for _lib in _libs:
    if not hasattr(_lib, 'IsAlignmentNeeded'):
        continue
    IsAlignmentNeeded = _lib.IsAlignmentNeeded
    IsAlignmentNeeded.argtypes = [POINTER(c_bool)]
    IsAlignmentNeeded.restype = ReturnStatus
    IsAlignmentNeeded.errcheck = error_check
    break

# RSA300API.h: 525
for _lib in _libs:
    if not hasattr(_lib, 'PLAYBACK_OpenDiskFile'):
        continue
    PLAYBACK_OpenDiskFile = _lib.PLAYBACK_OpenDiskFile
    PLAYBACK_OpenDiskFile.argtypes = [POINTER(c_wchar), c_int, c_int, c_double, c_bool, c_bool]
    PLAYBACK_OpenDiskFile.restype = ReturnStatus
    PLAYBACK_OpenDiskFile.errcheck = error_check
    break

# RSA300API.h: 533
for _lib in _libs:
    if not hasattr(_lib, 'PLAYBACK_HasReplayCompleted'):
        continue
    PLAYBACK_HasReplayCompleted = _lib.PLAYBACK_HasReplayCompleted
    PLAYBACK_HasReplayCompleted.argtypes = [POINTER(c_bool)]
    PLAYBACK_HasReplayCompleted.restype = ReturnStatus
    PLAYBACK_HasReplayCompleted.errcheck = error_check
    break

enum_anon_27 = c_int # RSA300API.h: 554

SpectrumWindow_Kaiser = 0 # RSA300API.h: 554

SpectrumWindow_Mil6dB = (SpectrumWindow_Kaiser + 1) # RSA300API.h: 554

SpectrumWindow_BlackmanHarris = (SpectrumWindow_Mil6dB + 1) # RSA300API.h: 554

SpectrumWindow_Rectangle = (SpectrumWindow_BlackmanHarris + 1) # RSA300API.h: 554

SpectrumWindow_FlatTop = (SpectrumWindow_Rectangle + 1) # RSA300API.h: 554

SpectrumWindow_Hann = (SpectrumWindow_FlatTop + 1) # RSA300API.h: 554

SpectrumWindows = enum_anon_27 # RSA300API.h: 554

enum_anon_28 = c_int # RSA300API.h: 562

SpectrumTrace1 = 0 # RSA300API.h: 562

SpectrumTrace2 = (SpectrumTrace1 + 1) # RSA300API.h: 562

SpectrumTrace3 = (SpectrumTrace2 + 1) # RSA300API.h: 562

SpectrumTraces = enum_anon_28 # RSA300API.h: 562

enum_anon_29 = c_int # RSA300API.h: 571

SpectrumDetector_PosPeak = 0 # RSA300API.h: 571

SpectrumDetector_NegPeak = (SpectrumDetector_PosPeak + 1) # RSA300API.h: 571

SpectrumDetector_AverageVRMS = (SpectrumDetector_NegPeak + 1) # RSA300API.h: 571

SpectrumDetector_Sample = (SpectrumDetector_AverageVRMS + 1) # RSA300API.h: 571

SpectrumDetectors = enum_anon_29 # RSA300API.h: 571

enum_anon_30 = c_int # RSA300API.h: 581

SpectrumVerticalUnit_dBm = 0 # RSA300API.h: 581

SpectrumVerticalUnit_Watt = (SpectrumVerticalUnit_dBm + 1) # RSA300API.h: 581

SpectrumVerticalUnit_Volt = (SpectrumVerticalUnit_Watt + 1) # RSA300API.h: 581

SpectrumVerticalUnit_Amp = (SpectrumVerticalUnit_Volt + 1) # RSA300API.h: 581

SpectrumVerticalUnit_dBmV = (SpectrumVerticalUnit_Amp + 1) # RSA300API.h: 581

SpectrumVerticalUnits = enum_anon_30 # RSA300API.h: 581

# RSA300API.h: 604
class struct_anon_31(Structure):
    pass

struct_anon_31.__slots__ = [
    'span',
    'rbw',
    'enableVBW',
    'vbw',
    'traceLength',
    'window',
    'verticalUnit',
    'actualStartFreq',
    'actualStopFreq',
    'actualFreqStepSize',
    'actualRBW',
    'actualVBW',
    'actualNumIQSamples',
]
struct_anon_31._fields_ = [
    ('span', c_double),
    ('rbw', c_double),
    ('enableVBW', c_bool),
    ('vbw', c_double),
    ('traceLength', c_int),
    ('window', SpectrumWindows),
    ('verticalUnit', SpectrumVerticalUnits),
    ('actualStartFreq', c_double),
    ('actualStopFreq', c_double),
    ('actualFreqStepSize', c_double),
    ('actualRBW', c_double),
    ('actualVBW', c_double),
    ('actualNumIQSamples', c_int),
]

Spectrum_Settings = struct_anon_31 # RSA300API.h: 604

# RSA300API.h: 617
class struct_anon_32(Structure):
    pass

struct_anon_32.__slots__ = [
    'maxSpan',
    'minSpan',
    'maxRBW',
    'minRBW',
    'maxVBW',
    'minVBW',
    'maxTraceLength',
    'minTraceLength',
]
struct_anon_32._fields_ = [
    ('maxSpan', c_double),
    ('minSpan', c_double),
    ('maxRBW', c_double),
    ('minRBW', c_double),
    ('maxVBW', c_double),
    ('minVBW', c_double),
    ('maxTraceLength', c_int),
    ('minTraceLength', c_int),
]

Spectrum_Limits = struct_anon_32 # RSA300API.h: 617

# RSA300API.h: 624
class struct_anon_33(Structure):
    pass

struct_anon_33.__slots__ = [
    'timestamp',
    'acqDataStatus',
]
struct_anon_33._fields_ = [
    ('timestamp', c_uint64),
    ('acqDataStatus', c_uint16),
]

Spectrum_TraceInfo = struct_anon_33 # RSA300API.h: 624

# RSA300API.h: 627
for _lib in _libs:
    if not hasattr(_lib, 'SPECTRUM_SetEnable'):
        continue
    SPECTRUM_SetEnable = _lib.SPECTRUM_SetEnable
    SPECTRUM_SetEnable.argtypes = [c_bool]
    SPECTRUM_SetEnable.restype = ReturnStatus
    SPECTRUM_SetEnable.errcheck = error_check
    break

# RSA300API.h: 628
for _lib in _libs:
    if not hasattr(_lib, 'SPECTRUM_GetEnable'):
        continue
    SPECTRUM_GetEnable = _lib.SPECTRUM_GetEnable
    SPECTRUM_GetEnable.argtypes = [POINTER(c_bool)]
    SPECTRUM_GetEnable.restype = ReturnStatus
    SPECTRUM_GetEnable.errcheck = error_check
    break

# RSA300API.h: 631
for _lib in _libs:
    if not hasattr(_lib, 'SPECTRUM_SetDefault'):
        continue
    SPECTRUM_SetDefault = _lib.SPECTRUM_SetDefault
    SPECTRUM_SetDefault.argtypes = []
    SPECTRUM_SetDefault.restype = ReturnStatus
    SPECTRUM_SetDefault.errcheck = error_check
    break

# RSA300API.h: 634
for _lib in _libs:
    if not hasattr(_lib, 'SPECTRUM_SetSettings'):
        continue
    SPECTRUM_SetSettings = _lib.SPECTRUM_SetSettings
    SPECTRUM_SetSettings.argtypes = [Spectrum_Settings]
    SPECTRUM_SetSettings.restype = ReturnStatus
    SPECTRUM_SetSettings.errcheck = error_check
    break

# RSA300API.h: 635
for _lib in _libs:
    if not hasattr(_lib, 'SPECTRUM_GetSettings'):
        continue
    SPECTRUM_GetSettings = _lib.SPECTRUM_GetSettings
    SPECTRUM_GetSettings.argtypes = [POINTER(Spectrum_Settings)]
    SPECTRUM_GetSettings.restype = ReturnStatus
    #SPECTRUM_GetSettings.errcheck = error_check # FIXME
    break

# RSA300API.h: 638
for _lib in _libs:
    if not hasattr(_lib, 'SPECTRUM_SetTraceType'):
        continue
    SPECTRUM_SetTraceType = _lib.SPECTRUM_SetTraceType
    SPECTRUM_SetTraceType.argtypes = [SpectrumTraces, c_bool, SpectrumDetectors]
    SPECTRUM_SetTraceType.restype = ReturnStatus
    SPECTRUM_SetTraceType.errcheck = error_check
    break

# RSA300API.h: 639
for _lib in _libs:
    if not hasattr(_lib, 'SPECTRUM_GetTraceType'):
        continue
    SPECTRUM_GetTraceType = _lib.SPECTRUM_GetTraceType
    SPECTRUM_GetTraceType.argtypes = [SpectrumTraces, POINTER(c_bool), POINTER(SpectrumDetectors)]
    SPECTRUM_GetTraceType.restype = ReturnStatus
    SPECTRUM_GetTraceType.errcheck = error_check
    break

# RSA300API.h: 642
for _lib in _libs:
    if not hasattr(_lib, 'SPECTRUM_GetLimits'):
        continue
    SPECTRUM_GetLimits = _lib.SPECTRUM_GetLimits
    SPECTRUM_GetLimits.argtypes = [POINTER(Spectrum_Limits)]
    SPECTRUM_GetLimits.restype = ReturnStatus
    SPECTRUM_GetLimits.errcheck = error_check
    break

# RSA300API.h: 645
for _lib in _libs:
    if not hasattr(_lib, 'SPECTRUM_WaitForDataReady'):
        continue
    SPECTRUM_WaitForDataReady = _lib.SPECTRUM_WaitForDataReady
    SPECTRUM_WaitForDataReady.argtypes = [c_int, POINTER(c_bool)]
    SPECTRUM_WaitForDataReady.restype = ReturnStatus
    SPECTRUM_WaitForDataReady.errcheck = error_check
    break

# RSA300API.h: 648
for _lib in _libs:
    if not hasattr(_lib, 'SPECTRUM_GetTrace'):
        continue
    SPECTRUM_GetTrace = _lib.SPECTRUM_GetTrace
    SPECTRUM_GetTrace.argtypes = [SpectrumTraces, c_int, POINTER(c_float), POINTER(c_int)]
    SPECTRUM_GetTrace.restype = ReturnStatus
    SPECTRUM_GetTrace.errcheck = error_check
    break

# RSA300API.h: 650
for _lib in _libs:
    if not hasattr(_lib, 'SPECTRUM_GetTraceInfo'):
        continue
    SPECTRUM_GetTraceInfo = _lib.SPECTRUM_GetTraceInfo
    SPECTRUM_GetTraceInfo.argtypes = [POINTER(Spectrum_TraceInfo)]
    SPECTRUM_GetTraceInfo.restype = ReturnStatus
    SPECTRUM_GetTraceInfo.errcheck = error_check
    break

# No inserted files

