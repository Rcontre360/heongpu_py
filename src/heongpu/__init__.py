
from enum import Enum
import _heongpu_api
from .ckks_tensor import CKKSTensor

# Re-export only necessary symbols from the C++ module
Ciphertext = _heongpu_api.Ciphertext
DeviceVector = _heongpu_api.DeviceVector
ExecutionOptions = _heongpu_api.ExecutionOptions
Galoiskey = _heongpu_api.Galoiskey
HEDecryptor = _heongpu_api.HEDecryptor
HEEncoder = _heongpu_api.HEEncoder
HEEncryptor = _heongpu_api.HEEncryptor
HEKeyGenerator = _heongpu_api.HEKeyGenerator
HEOperator = _heongpu_api.HEOperator
HostVector = _heongpu_api.HostVector
KeySwitchingType = _heongpu_api.KeySwitchingType
MultipartyPublickey = _heongpu_api.MultipartyPublickey
Parameters = _heongpu_api.Parameters
Plaintext = _heongpu_api.Plaintext
Publickey = _heongpu_api.Publickey
Relinkey = _heongpu_api.Relinkey
SchemeType = _heongpu_api.SchemeType
SecretKey = _heongpu_api.SecretKey
SecurityLevel = _heongpu_api.SecurityLevel
Switchkey = _heongpu_api.Switchkey
VecDouble = _heongpu_api.VecDouble
VecInt = _heongpu_api.VecInt
VecUint = _heongpu_api.VecUint
get_device_count = _heongpu_api.get_device_count
set_device = _heongpu_api.set_device

# Do NOT expose these directly in the namespace
_SCHEME_BFV = _heongpu_api.SchemeType.BFV
_SCHEME_CKKS = _heongpu_api.SchemeType.CKKS
_SCHEME_BGV = _heongpu_api.SchemeType.BGV

_KS_METHOD_I = _heongpu_api.KeySwitchingType.METHOD_I
_KS_METHOD_II = _heongpu_api.KeySwitchingType.METHOD_II
_KS_METHOD_III = _heongpu_api.KeySwitchingType.METHOD_III
_KS_NONE = _heongpu_api.KeySwitchingType.NONE

_SEC_128 = _heongpu_api.SecurityLevel.SEC128
_SEC_192 = _heongpu_api.SecurityLevel.SEC192
_SEC_256 = _heongpu_api.SecurityLevel.SEC256

class SCHEMES(Enum):
    BFV = _heongpu_api.BFV,
    CKKS = _heongpu_api.CKKS,
    BGV = _heongpu_api.BGV,

class KEY_SWITCHING_TYPES(Enum):
    METHOD_I = _heongpu_api.METHOD_I,
    METHOD_II = _heongpu_api.METHOD_II,
    METHOD_III = _heongpu_api.METHOD_III,
    NONE = _heongpu_api.NONE,

class SECURITY_LEVELS(Enum):
    SEC128 = _heongpu_api.SEC128,
    SEC192 = _heongpu_api.SEC192,
    SEC256 = _heongpu_api.SEC256,

__all__ = [
    "CKKSTensor",
    "Ciphertext",
    "DeviceVector",
    "ExecutionOptions",
    "Galoiskey",
    "HEDecryptor",
    "HEEncoder",
    "HEEncryptor",
    "HEKeyGenerator",
    "HEOperator",
    "HostVector",
    "KeySwitchingType",
    "MultipartyPublickey",
    "Parameters",
    "Plaintext",
    "Publickey",
    "Relinkey",
    "SchemeType",
    "SecretKey",
    "SecurityLevel",
    "Switchkey",
    "VecDouble",
    "VecInt",
    "VecUint",
    "get_device_count",
    "set_device",
    "SCHEMES",
    "KEY_SWITCHING_TYPES",
    "SECURITY_LEVELS",
]
