from heongpu import _heongpu_api

class CKKSTensor:
    def __init__(self, context: _heongpu_api.Parameters, data: list[float], scale: float, public_key: _heongpu_api.Publickey):
        self.context = context
        self.scale = scale
        self.encoder = _heongpu_api.HEEncoder(context)
        self.encryptor = _heongpu_api.HEEncryptor(context, public_key)
        self.operators = _heongpu_api.HEOperator(context)

        # Store encoded plaintext
        self.plain = _heongpu_api.Plaintext(context)
        vec = _heongpu_api.VecDouble(data)
        self.encoder.encode(self.plain, vec, self.scale)

        # Encrypt plaintext
        self.ctxt = _heongpu_api.Ciphertext(context)
        self.encryptor.encrypt(self.ctxt, self.plain)

        self.relin_key = None
        self.exec_opts = _heongpu_api.ExecutionOptions()

    def set_relin_key(self, relin_key: _heongpu_api.Relinkey):
        self.relin_key = relin_key

    def decrypt(self, secret_key: _heongpu_api.SecretKey) -> list[float]:
        decryptor = _heongpu_api.HEDecryptor(self.context, secret_key)
        self.plain = _heongpu_api.Plaintext(self.context)
        decryptor.decrypt(self.plain, self.ctxt)

        decoded = _heongpu_api.VecDouble([])
        self.encoder.decode(decoded, self.plain)
        return [decoded[i] for i in range(len(decoded))]

    def __add__(self, other: 'CKKSTensor') -> 'CKKSTensor':
        result_ctxt = _heongpu_api.Ciphertext(self.context)
        self.operators.add(self.ctxt, other.ctxt, result_ctxt, self.exec_opts)
        return CKKSTensor.from_ciphertext(self.context, result_ctxt, self.scale, self.encoder, self.operators, self.relin_key)

    def __iadd__(self, other: 'CKKSTensor'):
        self.operators.add_inplace(self.ctxt, other.ctxt, self.exec_opts)
        return self

    def __sub__(self, other: 'CKKSTensor') -> 'CKKSTensor':
        result_ctxt = _heongpu_api.Ciphertext(self.context)
        self.operators.sub(self.ctxt, other.ctxt, result_ctxt, self.exec_opts)
        return CKKSTensor.from_ciphertext(self.context, result_ctxt, self.scale, self.encoder, self.operators, self.relin_key)

    def __isub__(self, other: 'CKKSTensor'):
        self.operators.sub_inplace(self.ctxt, other.ctxt, self.exec_opts)
        return self

    def __mul__(self, other: 'CKKSTensor') -> 'CKKSTensor':
        result_ctxt = _heongpu_api.Ciphertext(self.context)
        self.operators.multiply(self.ctxt, other.ctxt, result_ctxt, self.exec_opts)
        if self.relin_key:
            self.operators.relinearize_inplace(result_ctxt, self.relin_key, self.exec_opts)
        return CKKSTensor.from_ciphertext(self.context, result_ctxt, self.scale, self.encoder, self.operators, self.relin_key)

    def __imul__(self, other: 'CKKSTensor'):
        self.operators.multiply_inplace(self.ctxt, other.ctxt, self.exec_opts)
        if self.relin_key:
            self.operators.relinearize_inplace(self.ctxt, self.relin_key, self.exec_opts)
        return self

    def __neg__(self) -> 'CKKSTensor':
        result_ctxt = _heongpu_api.Ciphertext(self.context)
        self.operators.negate(self.ctxt, result_ctxt, self.exec_opts)
        return CKKSTensor.from_ciphertext(self.context, result_ctxt, self.scale, self.encoder, self.operators, self.relin_key)

    def __str__(self):
        return "<CKKSTensor (encrypted)>"

    def decrypted_str(self, secret_key: _heongpu_api.SecretKey, max_items: int = 10) -> str:
        values = self.decrypt(secret_key)
        return f"<CKKSTensor {values[:max_items]}...>"

    @classmethod
    def from_ciphertext(cls, context, ctxt, scale, encoder, operators, relin_key):
        obj = cls.__new__(cls)
        obj.context = context
        obj.scale = scale
        obj.encoder = encoder
        obj.operators = operators
        obj.ctxt = ctxt
        obj.relin_key = relin_key
        obj.exec_opts = _heongpu_api.ExecutionOptions()
        obj.plain = None  # will be set on decryption
        return obj

