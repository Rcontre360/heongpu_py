from heongpu import _heongpu_api

class CKKSContext:
    parameters: _heongpu_api.Parameters
    public_key: _heongpu_api.Publickey
    private_key: _heongpu_api.SecretKey
    relin_key: _heongpu_api.Relinkey
    scale: float

    def __init__(self, poly_modulus_degree:int, scale:int, coeff_mod_bit_sizes: list[int]):
        _heongpu_api.set_device(0)
        self.scale = scale
        self.parameters = _heongpu_api.Parameters(_heongpu_api.CKKS,_heongpu_api.METHOD_I)

        self.parameters.set_poly_modulus_degree(poly_modulus_degree)
        self.parameters.set_coeff_modulus(coeff_mod_bit_sizes,[ 60 ])

        self.parameters.generate()

    def generate_keys(self):
        keygen = _heongpu_api.HEKeyGenerator(self.parameters)
        self.private_key = _heongpu_api.SecretKey(self.parameters)
        self.public_key = _heongpu_api.Publickey(self.parameters)
        self.relin_key = _heongpu_api.Relinkey(self.parameters)

        keygen.generate_secret_key(self.private_key)
        keygen.generate_public_key(self.public_key, self.private_key)
        keygen.generate_relin_key(self.relin_key, self.private_key)

    def print_ckks_params(self):
        self.parameters.print_parameters()

class CKKSTensor:
    context: CKKSContext

    def __init__(self, context: CKKSContext, data:list[float]):
        self.context = context
        self.encoder = _heongpu_api.HEEncoder(self.context.parameters)
        self.encryptor = _heongpu_api.HEEncryptor(self.context.parameters, context.public_key)
        self.operators = _heongpu_api.HEOperator(self.context.parameters)

        # Store encoded plaintext
        self.plain = _heongpu_api.Plaintext(self.context.parameters)
        vec = _heongpu_api.VecDouble(data)
        self.encoder.encode(self.plain, vec, self.context.scale)

        # Encrypt plaintext
        self.ctxt = _heongpu_api.Ciphertext(self.context.parameters)
        self.encryptor.encrypt(self.ctxt, self.plain)

        self.exec_opts = _heongpu_api.ExecutionOptions()

    def decrypt(self) -> list[float]:
        decryptor = _heongpu_api.HEDecryptor(self.context.parameters, self.context.private_key)
        self.plain = _heongpu_api.Plaintext(self.context.parameters)
        decryptor.decrypt(self.plain, self.ctxt)

        decoded = _heongpu_api.VecDouble([])
        self.encoder.decode(decoded, self.plain)
        return [decoded[i] for i in range(len(decoded))]

    def __add__(self, other: 'CKKSTensor') -> 'CKKSTensor':
        result_ctxt = _heongpu_api.Ciphertext(self.context.parameters)
        self.operators.add(self.ctxt, other.ctxt, result_ctxt, self.exec_opts)
        return CKKSTensor.from_ciphertext(self.context, result_ctxt)

    def __iadd__(self, other: 'CKKSTensor'):
        self.operators.add_inplace(self.ctxt, other.ctxt, self.exec_opts)
        return self

    def __sub__(self, other: 'CKKSTensor') -> 'CKKSTensor':
        result_ctxt = _heongpu_api.Ciphertext(self.context.parameters)
        self.operators.sub(self.ctxt, other.ctxt, result_ctxt, self.exec_opts)
        return CKKSTensor.from_ciphertext(self.context, result_ctxt)

    def __isub__(self, other: 'CKKSTensor'):
        self.operators.sub_inplace(self.ctxt, other.ctxt, self.exec_opts)
        return self

    def __mul__(self, other: 'CKKSTensor') -> 'CKKSTensor':
        result_ctxt = _heongpu_api.Ciphertext(self.context.parameters)
        self.operators.multiply(self.ctxt, other.ctxt, result_ctxt, self.exec_opts)
        self.operators.relinearize_inplace(result_ctxt, self.context.relin_key, self.exec_opts)
        return CKKSTensor.from_ciphertext(self.context, result_ctxt)

    def __imul__(self, other: 'CKKSTensor'):
        self.operators.multiply_inplace(self.ctxt, other.ctxt, self.exec_opts)
        self.operators.relinearize_inplace(self.ctxt, self.context.relin_key, self.exec_opts)
        return self

    def __neg__(self) -> 'CKKSTensor':
        result_ctxt = _heongpu_api.Ciphertext(self.context.parameters)
        self.operators.negate(self.ctxt, result_ctxt, self.exec_opts)
        return CKKSTensor.from_ciphertext(self.context, result_ctxt)

    def __str__(self):
        return "<CKKSTensor (encrypted)>"

    def decrypted_str(self,  max_items: int = 10) -> str:
        values = self.decrypt(self.context.private_key)
        return f"<CKKSTensor {values[:max_items]}...>"

    @classmethod
    def from_ciphertext(cls, context:CKKSContext, ctxt:_heongpu_api.Ciphertext):
        obj = cls.__new__(cls)
        obj.context = context
        obj.encoder = _heongpu_api.HEEncoder(context.parameters)
        obj.encryptor = _heongpu_api.HEEncryptor(context.parameters, context.public_key)
        obj.operators = _heongpu_api.HEOperator(context.parameters)
        obj.exec_opts = _heongpu_api.ExecutionOptions()

        obj.ctxt = ctxt
        obj.exec_opts = _heongpu_api.ExecutionOptions()
        obj.plain = None  # will be set on decryption

        return obj


