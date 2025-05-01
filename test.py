from heongpu import  HEKeyGenerator, set_device, CKKSTensor,Publickey, SecretKey, Parameters, SCHEMES, KEY_SWITCHING_TYPES, SECURITY_LEVELS
from heongpu import _heongpu_api
import numpy as np

set_device(0)
context = Parameters(_heongpu_api.CKKS, _heongpu_api.METHOD_I)
poly_modulus_degree = 32768
coeff_mod_bit_sizes = [60, 40, 40, 60]
scale = 2**40
vec_size = 4096
repetitions = 100

context.set_poly_modulus_degree(poly_modulus_degree)
context.set_coeff_modulus(coeff_mod_bit_sizes,[ 60 ])

context.generate()
context.print_parameters()

keygen = HEKeyGenerator(context)
secret_key = SecretKey(context)
public_key = Publickey(context)

keygen.generate_secret_key(secret_key)
keygen.generate_public_key(public_key, secret_key)

message = [i + 10 for i in range(100)]
t1 = CKKSTensor(context, message, scale, public_key)

message2 = [i + 20 for i in range(100)]
t2 = CKKSTensor(context, message2, scale, public_key)

t3 = t1+t2

print(t3.decrypt(secret_key)[0:10])

