from heongpu import  HEKeyGenerator, set_device, Publickey, SecretKey, Parameters, SCHEMES, KEY_SWITCHING_TYPES, SECURITY_LEVELS
from heongpu import _heongpu_api
from ckks import CKKSContext, CKKSTensor

poly_modulus_degree = 32768
coeff_mod_bit_sizes = [60, 40, 40, 60]
scale = 2**40
vec_size = 4096
repetitions = 100

context = CKKSContext(poly_modulus_degree, scale, coeff_mod_bit_sizes)
context.generate_keys()
context.print_ckks_params()

message = [i for i in range(100)]
t1 = CKKSTensor(context, message)

message2 = [i for i in range(100)]
t2 = CKKSTensor(context, message2)

t2 -= t1

print(t2.decrypt()[0:10])

