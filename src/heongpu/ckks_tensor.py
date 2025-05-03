import typing
from heongpu import _heongpu_api

class CKKSContext:
    parameters: _heongpu_api.Parameters
    public_key: _heongpu_api.Publickey
    private_key: _heongpu_api.SecretKey
    galois_key: _heongpu_api.Galoiskey
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
        self.galois_key = _heongpu_api.Galoiskey(self.parameters)

        keygen.generate_secret_key(self.private_key)
        keygen.generate_public_key(self.public_key, self.private_key)
        keygen.generate_relin_key(self.relin_key, self.private_key)
        keygen.generate_galois_key(self.galois_key, self.private_key)

    def print_ckks_params(self):
        self.parameters.print_parameters()

class CKKSTensor:
    size:int
    context: CKKSContext
    encoder: _heongpu_api.HEEncoder
    encryptor: _heongpu_api.HEEncryptor
    operators: _heongpu_api.HEOperator
    ctxt: _heongpu_api.Ciphertext

    def __init__(self, context: CKKSContext, data:list[float]):
        self.size = len(data)
        self.context = context
        self.encoder = _heongpu_api.HEEncoder(self.context.parameters)
        self.encryptor = _heongpu_api.HEEncryptor(self.context.parameters, context.public_key)
        self.decryptor = _heongpu_api.HEDecryptor(self.context.parameters, self.context.private_key)
        self.operators = _heongpu_api.HEOperator(self.context.parameters)

        # Store encoded plaintext
        plain = _heongpu_api.Plaintext(self.context.parameters)
        self.encoder.encode(plain,_heongpu_api.VecDouble(data), self.context.scale)

        # Encrypt plaintext
        self.ctxt = _heongpu_api.Ciphertext(self.context.parameters)
        self.encryptor.encrypt(self.ctxt, plain)

        self.exec_opts = _heongpu_api.ExecutionOptions()

    def decrypt(self) -> list[float]:
        return self._decrypt(self.ctxt)

    def _decrypt(self, ctxt: _heongpu_api.Ciphertext) -> list[float]:
        plain = _heongpu_api.Plaintext(self.context.parameters)
        self.decryptor.decrypt(plain, ctxt, self.exec_opts)

        decoded = _heongpu_api.VecDouble([])
        self.encoder.decode(decoded, plain)
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

    def __mul__(self, other:  typing.Union['CKKSTensor', list[float]]) -> 'CKKSTensor':
        if isinstance(other, CKKSTensor):
            result_ctxt = _heongpu_api.Ciphertext(self.context.parameters)
            self.operators.multiply(self.ctxt, other.ctxt, result_ctxt, self.exec_opts)
            self.operators.relinearize_inplace(result_ctxt, self.context.relin_key, self.exec_opts)
            self.operators.rescale_inplace(result_ctxt, self.exec_opts)
            return CKKSTensor.from_ciphertext(self.context, result_ctxt)
        elif isinstance(other, list) and all(isinstance(x, (int, float)) for x in other):
            result_ctxt = _heongpu_api.Ciphertext(self.context.parameters)
            plain = _heongpu_api.Plaintext(self.context.parameters)
            self.encoder.encode(plain,_heongpu_api.VecDouble(other), self.context.scale)

            self.operators.multiply_plain(self.ctxt, plain, result_ctxt, self.exec_opts)
            return CKKSTensor.from_ciphertext(self.context, result_ctxt)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'CKKSTensor' and '{type(other).__name__}'")

    def __imul__(self, other: 'CKKSTensor'):
        if isinstance(other, CKKSTensor):
            self.operators.multiply_inplace(self.ctxt, other.ctxt, self.exec_opts)
            self.operators.relinearize_inplace(self.ctxt, self.context.relin_key, self.exec_opts)
        elif isinstance(other, list) and all(isinstance(x, (int, float)) for x in other):
            plain = _heongpu_api.Plaintext(self.context.parameters)
            self.encoder.encode(plain,_heongpu_api.VecDouble(other), self.context.scale)
            self.operators.multiply_plain_inplace(self.ctxt, plain, self.exec_opts)
            self.operators.rescale_inplace(self.ctxt, self.exec_opts)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'CKKSTensor' and '{type(other).__name__}'")
        return self

    def __neg__(self) -> 'CKKSTensor':
        result_ctxt = _heongpu_api.Ciphertext(self.context.parameters)
        self.operators.negate(self.ctxt, result_ctxt, self.exec_opts)
        return CKKSTensor.from_ciphertext(self.context, result_ctxt)

    def __str__(self):
        return "<CKKSTensor (encrypted)>"

    def __matmul__(self, matrix: list[list[float]]) -> 'CKKSTensor':
        def decompose_matrix(matrix: list[list[float]]) -> list[list[float]]:
            n = len(matrix)
            res = [[] for _ in range(n)]

            for i in range(1,n):
                cur_i = 0
                cur_j = i
                for plus in range(n-i):
                    res[i].append(matrix[cur_i + plus][cur_j + plus])

            for i in range(n):
                cur_i = i
                cur_j = 0
                for plus in range(n - cur_i):
                    res[(n-i)%n].append(matrix[cur_i + plus][cur_j + plus])

            return res

        ctxt = _heongpu_api.Ciphertext(self.ctxt)
        t1 = CKKSTensor.from_ciphertext(self.context,ctxt)
        [a,b,c,d] = decompose_matrix(matrix)

        a = t1 * a
        t1.rotate_inplace()
        b = t1 * b
        t1.rotate_inplace()
        c = t1 * c
        t1.rotate_inplace()
        d = t1 * d

        return a + b + c + d

    def dot(self, coef: list[float]) -> 'CKKSTensor':
        multiplied = self * coef

        self.operators.rescale_inplace(multiplied.ctxt, self.exec_opts)
        accum_ctxt = _heongpu_api.Ciphertext(multiplied.ctxt)

        # Rotate and accumulate
        for i in range(1,self.size):
            self.operators.rotate_rows_inplace(multiplied.ctxt, self.context.galois_key, 1, self.exec_opts)
            self.operators.add_inplace(accum_ctxt, multiplied.ctxt, self.exec_opts)

        return CKKSTensor.from_ciphertext(self.context, accum_ctxt)

    # only works when places is a power of 2
    def rotate(self,  places=1) -> 'CKKSTensor':
        result_ctxt = _heongpu_api.Ciphertext(self.context.parameters)
        self.operators.rotate_rows(self.ctxt, result_ctxt, self.context.galois_key, places, self.exec_opts)
        return CKKSTensor.from_ciphertext(self.context, result_ctxt)

    def rotate_inplace(self,  places=1):
        self.operators.rotate_rows_inplace(self.ctxt, self.context.galois_key, places, self.exec_opts)

    def decrypted_str(self,  max_items: int = 10) -> str:
        values = self.decrypt(self.context.private_key)
        return f"<CKKSTensor {values[:max_items]}...>"

    def decrypted_str(self,  max_items: int = 10) -> str:
        values = self.decrypt(self.context.private_key)
        return f"<CKKSTensor {values[:max_items]}...>"

    @classmethod
    def from_ciphertext(cls, context:CKKSContext, ctxt:_heongpu_api.Ciphertext):
        obj = cls.__new__(cls)
        obj.context = context
        obj.encoder = _heongpu_api.HEEncoder(context.parameters)
        obj.encryptor = _heongpu_api.HEEncryptor(context.parameters, context.public_key)
        obj.decryptor = _heongpu_api.HEDecryptor(context.parameters, context.private_key)
        obj.operators = _heongpu_api.HEOperator(context.parameters)
        obj.exec_opts = _heongpu_api.ExecutionOptions()

        obj.ctxt = ctxt
        obj.exec_opts = _heongpu_api.ExecutionOptions()
        obj.plain = None  # will be set on decryption

        return obj

