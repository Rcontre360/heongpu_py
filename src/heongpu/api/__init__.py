from typing import Dict, Any

try:
    import _heongpu_api
except ImportError as e:
    raise ImportError("Failed to import compiled module '_heongpu_api'. Make sure it is built.") from e

class Ciphertext:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, context: Parameters, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def __init__(self, cipher: list[int], context: Parameters, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def __init__(self, cipher: HostVector, context: Parameters, options: ExecutionOptions = ...) -> None:
        ...
    def coeff_modulus_count(self) -> int:
        ...
    def data(self) -> int:
        ...
    def depth(self) -> int:
        ...
    def get_data(self, cipher: list[int], stream_ptr: int = 0) -> None:
        ...
    def get_data_host(self, cipher: HostVector, stream_ptr: int = 0) -> None:
        ...
    def in_ntt_domain(self) -> bool:
        ...
    def is_on_device(self) -> bool:
        ...
    def relinearization_required(self) -> bool:
        ...
    def rescale_required(self) -> bool:
        ...
    def ring_size(self) -> int:
        ...
    def scale(self) -> float:
        ...
    def size(self) -> int:
        ...
    def store_in_device(self, stream_ptr: int = 0) -> None:
        ...
    def store_in_host(self, stream_ptr: int = 0) -> None:
        ...
    def stream(self) -> int:
        ...
    def switch_stream(self, stream_ptr: int) -> None:
        ...

class DeviceVector:
    def __getitem__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, size: int, stream_ptr: int = 0) -> None:
        ...
    @typing.overload
    def __init__(self, vector: list[int], stream_ptr: int = 0) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    def append(self, other: DeviceVector, stream_ptr: int = 0) -> None:
        ...
    def data(self) -> int:
        ...
    def reserve(self, new_size: int, stream_ptr: int = 0) -> None:
        ...
    def resize(self, new_size: int, stream_ptr: int = 0) -> None:
        ...

class ExecutionOptions:
    def __init__(self) -> None:
        ...
    def set_initial_location(self, keep_initial_condition: bool) -> ExecutionOptions:
        ...
    def set_storage_type(self, storage: ...) -> ExecutionOptions:
        ...
    def set_stream(self, stream_ptr: int) -> ExecutionOptions:
        ...
    @property
    def keep_initial_condition(self) -> bool:
        """
        Whether to maintain initial data location.
        """
    @keep_initial_condition.setter
    def keep_initial_condition(self, arg1: bool) -> None:
        ...
    @property
    def storage(self) -> ...:
        """
        Storage type to use (DEVICE or HOST).
        """
    @storage.setter
    def storage(self, arg1: ...) -> None:
        ...
    @property
    def stream(self) -> int:
        """
        CUDA stream to be used for execution.
        """
    @stream.setter
    def stream(self, arg1: int) -> None:
        ...

class Galoiskey:
    @typing.overload
    def __init__(self, context: Parameters, store_in_gpu: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, context: Parameters, shift_vec: list[int], store_in_gpu: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, context: Parameters, galois_elts: list[int], store_in_gpu: bool = True) -> None:
        ...
    def c_data(self) -> int:
        ...
    def data(self, i: int) -> int:
        ...
    def is_on_device(self) -> bool:
        ...
    def store_in_device(self, stream: int = 0) -> None:
        ...
    def store_in_host(self, stream: int = 0) -> None:
        ...

class HEDecryptor:
    def __init__(self, context: Parameters, secret_key: SecretKey) -> None:
        ...
    def decrypt(self, plaintext: Plaintext, ciphertext: ..., options: ExecutionOptions = ...) -> None:
        ...
    def get_offset(self) -> int:
        ...
    def get_seed(self) -> int:
        ...
    def multi_party_decrypt_fusion(self, ciphertexts: list[...], plaintext: Plaintext, options: ExecutionOptions = ...) -> None:
        ...
    def remainder_noise_budget(self, ciphertext: ..., options: ExecutionOptions = ...) -> int:
        ...
    def set_offset(self, arg0: int) -> None:
        ...
    def set_seed(self, arg0: int) -> None:
        ...

class HEEncoder:
    def __init__(self, context: Parameters) -> None:
        ...
    @typing.overload
    def decode(self, message: VecUint, plain: Plaintext, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def decode(self, message: VecInt, plain: Plaintext, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def decode(self, message: ..., plain: Plaintext, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def decode(self, message: ..., plain: Plaintext, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def decode(self, message: VecDouble, plain: Plaintext, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def decode(self, message: ..., plain: Plaintext, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def encode(self, plain: Plaintext, message: VecUint, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def encode(self, plain: Plaintext, message: VecInt, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def encode(self, plain: Plaintext, message: ..., options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def encode(self, plain: Plaintext, message: ..., options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def encode(self, plain: Plaintext, message: VecDouble, scale: float, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def encode(self, plain: Plaintext, message: ..., scale: float, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def encode(self, plain: Plaintext, message: float, scale: float, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def encode(self, plain: Plaintext, message: int, scale: float, options: ExecutionOptions = ...) -> None:
        ...
    def slot_count(self) -> int:
        ...

class HEEncryptor:
    def __init__(self, context: Parameters, public_key: Publickey) -> None:
        ...
    def encrypt(self, ciphertext: ..., plaintext: Plaintext, options: ExecutionOptions = ...) -> None:
        ...
    def get_offset(self) -> int:
        ...
    def get_seed(self) -> int:
        ...
    def set_offset(self, arg0: int) -> None:
        ...
    def set_seed(self, arg0: int) -> None:
        ...

class HEKeyGenerator:
    def __init__(self, context: Parameters) -> None:
        ...
    def generate_galois_key(self, gk: Galoiskey, sk: SecretKey, stream_ptr: int = 0) -> None:
        ...
    def generate_public_key(self, pk: Publickey, sk: SecretKey, stream_ptr: int = 0) -> None:
        ...
    def generate_relin_key(self, rk: Relinkey, sk: SecretKey, stream_ptr: int = 0) -> None:
        ...
    def generate_secret_key(self, sk: SecretKey, stream_ptr: int = 0) -> None:
        ...
    def generate_switch_key(self, swk: Switchkey, new_sk: SecretKey, old_sk: SecretKey, stream_ptr: int = 0) -> None:
        ...
    def get_offset(self) -> int:
        ...
    def get_seed(self) -> int:
        ...
    def set_offset(self, arg0: int) -> None:
        ...
    def set_seed(self, arg0: int) -> None:
        ...

class HEOperator:
    def __init__(self, context: Parameters) -> None:
        ...
    def add(self, arg0: ..., arg1: ..., arg2: ..., arg3: ExecutionOptions) -> None:
        ...
    def add_inplace(self, arg0: ..., arg1: ..., arg2: ExecutionOptions) -> None:
        ...
    def apply_galois(self, arg0: ..., arg1: ..., arg2: Galoiskey, arg3: int, arg4: ExecutionOptions) -> None:
        ...
    def apply_galois_inplace(self, arg0: ..., arg1: Galoiskey, arg2: int, arg3: ExecutionOptions) -> None:
        ...
    def conjugate(self, arg0: ..., arg1: ..., arg2: Galoiskey, arg3: ExecutionOptions) -> None:
        ...
    def keyswitch(self, arg0: ..., arg1: ..., arg2: Switchkey, arg3: ExecutionOptions) -> None:
        ...
    @typing.overload
    def mod_drop(self, arg0: ..., arg1: ..., arg2: ExecutionOptions) -> None:
        ...
    @typing.overload
    def mod_drop(self, arg0: Plaintext, arg1: Plaintext, arg2: ExecutionOptions) -> None:
        ...
    @typing.overload
    def mod_drop_inplace(self, arg0: Plaintext, arg1: ExecutionOptions) -> None:
        ...
    @typing.overload
    def mod_drop_inplace(self, arg0: ..., arg1: ExecutionOptions) -> None:
        ...
    def multiply(self, arg0: ..., arg1: ..., arg2: ..., arg3: ExecutionOptions) -> None:
        ...
    def multiply_inplace(self, arg0: ..., arg1: ..., arg2: ExecutionOptions) -> None:
        ...
    def multiply_plain(self, arg0: ..., arg1: Plaintext, arg2: ..., arg3: ExecutionOptions) -> None:
        ...
    def multiply_plain_inplace(self, arg0: ..., arg1: Plaintext, arg2: ExecutionOptions) -> None:
        ...
    def multiply_power_of_X(self, arg0: ..., arg1: ..., arg2: int, arg3: ExecutionOptions) -> None:
        ...
    def negate(self, arg0: ..., arg1: ..., arg2: ExecutionOptions) -> None:
        ...
    def negate_inplace(self, arg0: ..., arg1: ExecutionOptions) -> None:
        ...
    def relinearize_inplace(self, arg0: ..., arg1: Relinkey, arg2: ExecutionOptions) -> None:
        ...
    def rescale_inplace(self, arg0: ..., arg1: ExecutionOptions) -> None:
        ...
    def rotate_columns(self, arg0: ..., arg1: ..., arg2: Galoiskey, arg3: ExecutionOptions) -> None:
        ...
    def rotate_rows(self, arg0: ..., arg1: ..., arg2: Galoiskey, arg3: int, arg4: ExecutionOptions) -> None:
        ...
    def rotate_rows_inplace(self, arg0: ..., arg1: Galoiskey, arg2: int, arg3: ExecutionOptions) -> None:
        ...
    def sub(self, arg0: ..., arg1: ..., arg2: ..., arg3: ExecutionOptions) -> None:
        ...
    def sub_inplace(self, arg0: ..., arg1: ..., arg2: ExecutionOptions) -> None:
        ...
    def transform_from_ntt(self, arg0: ..., arg1: ..., arg2: ExecutionOptions) -> None:
        ...
    def transform_from_ntt_inplace(self, arg0: ..., arg1: ExecutionOptions) -> None:
        ...
    @typing.overload
    def transform_to_ntt(self, arg0: Plaintext, arg1: Plaintext, arg2: ExecutionOptions) -> None:
        ...
    @typing.overload
    def transform_to_ntt(self, arg0: ..., arg1: ..., arg2: ExecutionOptions) -> None:
        ...
    @typing.overload
    def transform_to_ntt_inplace(self, arg0: Plaintext, arg1: ExecutionOptions) -> None:
        ...
    @typing.overload
    def transform_to_ntt_inplace(self, arg0: ..., arg1: ExecutionOptions) -> None:
        ...

class HostVector:
    def __getitem__(self, arg0: int) -> int:
        ...
    def __init__(self) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    def get(self, index: int) -> int:
        ...
    def resize(self, arg0: int) -> None:
        ...

class KeySwitchingType:
    """
    Members:
    
      NONE
    
      METHOD_I
    
      METHOD_II
    
      METHOD_III
    """
    METHOD_I: typing.ClassVar[KeySwitchingType]  # value = <KeySwitchingType.METHOD_I: 1>
    METHOD_II: typing.ClassVar[KeySwitchingType]  # value = <KeySwitchingType.METHOD_II: 2>
    METHOD_III: typing.ClassVar[KeySwitchingType]  # value = <KeySwitchingType.METHOD_III: 3>
    NONE: typing.ClassVar[KeySwitchingType]  # value = <KeySwitchingType.NONE: 0>
    __members__: typing.ClassVar[dict[str, KeySwitchingType]]  # value = {'NONE': <KeySwitchingType.NONE: 0>, 'METHOD_I': <KeySwitchingType.METHOD_I: 1>, 'METHOD_II': <KeySwitchingType.METHOD_II: 2>, 'METHOD_III': <KeySwitchingType.METHOD_III: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...

class MultipartyPublickey(Publickey):
    def __init__(self, arg0: Parameters, arg1: int) -> None:
        ...
    def seed(self) -> int:
        ...

class Parameters:
    def __init__(self, scheme: SchemeType, ks_type: KeySwitchingType, sec_level: SecurityLevel = ...) -> None:
        ...
    def generate(self) -> None:
        ...
    def print_parameters(self) -> None:
        ...
    def set_coeff_modulus(self, arg0: list[int], arg1: list[int]) -> None:
        ...
    def set_default_coeff_modulus(self, arg0: int) -> None:
        ...
    def set_plain_modulus(self, arg0: int) -> None:
        ...
    def set_poly_modulus_degree(self, arg0: int) -> None:
        ...
    @property
    def ciphertext_modulus_count(self) -> int:
        ...
    @property
    def key_modulus(self) -> list[...]:
        ...
    @property
    def key_modulus_count(self) -> int:
        ...
    @property
    def log_poly_modulus_degree(self) -> int:
        ...
    @property
    def plain_modulus(self) -> ...:
        ...
    @property
    def poly_modulus_degree(self) -> int:
        ...

class Plaintext:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, context: Parameters, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def __init__(self, plain: list[int], context: Parameters, options: ExecutionOptions = ...) -> None:
        ...
    @typing.overload
    def __init__(self, plain: HostVector, context: Parameters, options: ExecutionOptions = ...) -> None:
        ...
    def data(self) -> int:
        ...
    def depth(self) -> int:
        ...
    def get_data(self, stream_ptr: int = 0) -> list[int]:
        ...
    def get_data_host_vector(self, stream_ptr: int = 0) -> HostVector:
        ...
    def in_ntt_domain(self) -> bool:
        ...
    def is_on_device(self) -> bool:
        ...
    def scale(self) -> float:
        ...
    def set_data(self, data: list[int]) -> None:
        ...
    def set_data_host_vector(self, data: HostVector) -> None:
        ...
    def size(self) -> int:
        ...
    def store_in_device(self, stream_ptr: int = 0) -> None:
        ...
    def store_in_host(self, stream_ptr: int = 0) -> None:
        ...

class Publickey:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Parameters) -> None:
        ...
    def coeff_modulus_count(self) -> int:
        ...
    def data(self) -> int:
        ...
    def device_to_host(self, public_key: list[int], stream_ptr: int = 0) -> None:
        ...
    def host_to_device(self, public_key: list[int], stream_ptr: int = 0) -> None:
        ...
    def ring_size(self) -> int:
        ...
    def stream(self) -> int:
        ...
    def switch_stream(self, stream_ptr: int = 0) -> None:
        ...

class Relinkey:
    @typing.overload
    def __init__(self, context: Parameters, store_in_gpu: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, context: Parameters, key: ..., store_in_gpu: bool = True) -> None:
        ...
    @typing.overload
    def __init__(self, context: Parameters, key: list[...], store_in_gpu: bool = True) -> None:
        ...
    @typing.overload
    def data(self) -> int:
        ...
    @typing.overload
    def data(self, i: int) -> int:
        ...
    def is_on_device(self) -> bool:
        ...
    def store_in_device(self, stream: int = 0) -> None:
        ...
    def store_in_host(self, stream: int = 0) -> None:
        ...

class SchemeType:
    """
    Members:
    
      BFV
    
      BGV
    
      CKKS
    """
    BFV: typing.ClassVar[SchemeType]  # value = <SchemeType.BFV: 1>
    BGV: typing.ClassVar[SchemeType]  # value = <SchemeType.BGV: 3>
    CKKS: typing.ClassVar[SchemeType]  # value = <SchemeType.CKKS: 2>
    __members__: typing.ClassVar[dict[str, SchemeType]]  # value = {'BFV': <SchemeType.BFV: 1>, 'BGV': <SchemeType.BGV: 3>, 'CKKS': <SchemeType.CKKS: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...

class SecretKey:
    @typing.overload
    def __init__(self, context: Parameters) -> None:
        ...
    @typing.overload
    def __init__(self, context: Parameters, hamming_weight: int) -> None:
        ...
    def coeff_modulus_count(self) -> int:
        ...
    def ring_size(self) -> int:
        ...
    def stream(self) -> int:
        ...
    def switch_stream(self, stream_ptr: int = 0) -> None:
        ...

class SecurityLevel:
    """
    Members:
    
      SEC128
    
      SEC192
    
      SEC256
    """
    SEC128: typing.ClassVar[SecurityLevel]  # value = <SecurityLevel.SEC128: 1>
    SEC192: typing.ClassVar[SecurityLevel]  # value = <SecurityLevel.SEC192: 2>
    SEC256: typing.ClassVar[SecurityLevel]  # value = <SecurityLevel.SEC256: 3>
    __members__: typing.ClassVar[dict[str, SecurityLevel]]  # value = {'SEC128': <SecurityLevel.SEC128: 1>, 'SEC192': <SecurityLevel.SEC192: 2>, 'SEC256': <SecurityLevel.SEC256: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...

class Switchkey:
    def __init__(self, context: Parameters, store_in_gpu: bool = True) -> None:
        ...
    def data(self) -> int:
        ...
    def is_on_device(self) -> bool:
        ...
    def store_in_device(self, stream: int = 0) -> None:
        ...
    def store_in_host(self, stream: int = 0) -> None:
        ...

class VecDouble:
    __hash__: typing.ClassVar[None] = None
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: float) -> bool:
        """
        Return true the container contains ``x``
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None:
        """
        Delete list elements using a slice object
        """
    def __eq__(self, arg0: VecDouble) -> bool:
        ...
    @typing.overload
    def __getitem__(self, s: slice) -> VecDouble:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: VecDouble) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None:
        ...
    def __iter__(self) -> typing.Iterator[float]:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: VecDouble) -> bool:
        ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this list.
        """
    @typing.overload
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: VecDouble) -> None:
        """
        Assign list elements using a slice object
        """
    def append(self, x: float) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: float) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: VecDouble) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    def insert(self, i: int, x: float) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> float:
        """
        Remove and return the last item
        """
    @typing.overload
    def pop(self, i: int) -> float:
        """
        Remove and return the item at index ``i``
        """
    def remove(self, x: float) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """

class VecInt:
    __hash__: typing.ClassVar[None] = None
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: int) -> bool:
        """
        Return true the container contains ``x``
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None:
        """
        Delete list elements using a slice object
        """
    def __eq__(self, arg0: VecInt) -> bool:
        ...
    @typing.overload
    def __getitem__(self, s: slice) -> VecInt:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: VecInt) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None:
        ...
    def __iter__(self) -> typing.Iterator[int]:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: VecInt) -> bool:
        ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this list.
        """
    @typing.overload
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: VecInt) -> None:
        """
        Assign list elements using a slice object
        """
    def append(self, x: int) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: int) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: VecInt) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    def insert(self, i: int, x: int) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> int:
        """
        Remove and return the last item
        """
    @typing.overload
    def pop(self, i: int) -> int:
        """
        Remove and return the item at index ``i``
        """
    def remove(self, x: int) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """

class VecUint:
    __hash__: typing.ClassVar[None] = None
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: int) -> bool:
        """
        Return true the container contains ``x``
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None:
        """
        Delete list elements using a slice object
        """
    def __eq__(self, arg0: VecUint) -> bool:
        ...
    @typing.overload
    def __getitem__(self, s: slice) -> VecUint:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: VecUint) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None:
        ...
    def __iter__(self) -> typing.Iterator[int]:
        ...
    def __len__(self) -> int:
        ...
    def __ne__(self, arg0: VecUint) -> bool:
        ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this list.
        """
    @typing.overload
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: VecUint) -> None:
        """
        Assign list elements using a slice object
        """
    def append(self, x: int) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: int) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: VecUint) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None:
        """
        Extend the list by appending all the items in the given list
        """
    def insert(self, i: int, x: int) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> int:
        """
        Remove and return the last item
        """
    @typing.overload
    def pop(self, i: int) -> int:
        """
        Remove and return the item at index ``i``
        """
    def remove(self, x: int) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
def get_device_count() -> int:
    """
    Get CUDA device count
    """
def set_device(arg0: int) -> None:
    """
    Set the active CUDA device
    """

SCHEMES: Dict[str, Any]
KEY_SWITCHING_TYPES: Dict[str, Any]
SECURITY_LEVELS: Dict[str, Any]

