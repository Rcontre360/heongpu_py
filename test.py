from heongpu import  HEKeyGenerator, set_device, Publickey, SecretKey, Parameters, SCHEMES, KEY_SWITCHING_TYPES, SECURITY_LEVELS
from heongpu import _heongpu_api
from ckks import CKKSContext, CKKSTensor
import copy

poly_modulus_degree = 32768
coeff_mod_bit_sizes = [60, 60, 60, 60]
scale = 2**50
vec_size = 100

context = CKKSContext(poly_modulus_degree, scale, coeff_mod_bit_sizes)
context.generate_keys()
context.print_ckks_params()

message = [i+1 for i in range(vec_size)] # [1, 2]
t1 = CKKSTensor(context, message)

message2 = [float(i+1) for i in range(vec_size)] # [1,2]
print(message,message2)

t3 = t1.dot(message2)

print("B: ",t3.decrypt()[0])

