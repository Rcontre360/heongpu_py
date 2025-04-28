import heongpu_py

heongpu_py.set_device(0)

# ['BFV', 'BGV', 'CKKS', 'Ciphertext', 'DeviceVector', 'ExecutionOptions', 'HEDecryptor', 'HEEncoder', 'HEEncryptor', 'HEKeyGenerator', 'HEOperator', 'HostVector', 'KeySwitchingType', 'METHOD_I', 'METHOD_II', 'METHOD_III', 'MultipartyPublickey', 'NONE', 'Parameters', 'Plaintext', 'Publickey', 'SEC128', 'SEC192', 'SEC256', 'SchemeType', 'SecretKey', 'SecurityLevel', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


context = heongpu_py.Parameters(heongpu_py.BFV,heongpu_py.METHOD_I)
poly_modulus_degree = 8192

context.set_poly_modulus_degree(poly_modulus_degree)
context.set_default_coeff_modulus(1)

plain_modulus = 1032193
context.set_plain_modulus(plain_modulus)
context.generate()
context.print_parameters()

keygen = heongpu_py.HEKeyGenerator(context)
secret_key = heongpu_py.SecretKey(context)
public_key = heongpu_py.Publickey(context)
relin_key = heongpu_py.Relinkey(context)

keygen.generate_secret_key(secret_key)
keygen.generate_public_key(public_key, secret_key)
keygen.generate_relin_key(relin_key, secret_key)

encoder = heongpu_py.HEEncoder(context)
encryptor = heongpu_py.HEEncryptor(context, public_key)
decryptor = heongpu_py.HEDecryptor(context, secret_key)
operators = heongpu_py.HEOperator(context)

row_size = poly_modulus_degree // 2;

print("Plaintext matrix row size: ", row_size)

message = [i for i in range(poly_modulus_degree)]

P1 = heongpu_py.Plaintext(context)
encoder.encode(P1,message)

C1 = heongpu_py.Ciphertext(context)
encryptor.encrypt(C1,P1)

print("Initial noise budget in C1: ", decryptor.remainder_noise_budget(C1))

operators.multiply_inplace(C1,C1,heongpu_py.ExecutionOptions())
operators.relinearize_inplace(C1, relin_key, heongpu_py.ExecutionOptions());

P2 = heongpu_py.Plaintext(context)
decryptor.decrypt(P2,C1)

check1 = heongpu_py.HostVector()
encoder.decode(check1,P2)

print("CHECK", check1.get(0))
