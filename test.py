from heongpu import  HEKeyGenerator, set_device, Publickey, SecretKey, Parameters, SCHEMES, KEY_SWITCHING_TYPES, SECURITY_LEVELS
from heongpu import _heongpu_api
from ckks import CKKSContext, CKKSTensor
import numpy as np

def print_ckks(vec:CKKSTensor, size:int):
    print(vec.decrypt()[:size])

poly_modulus_degree = 32768
coeff_mod_bit_sizes = [60, 60, 60, 60]
scale = 2**50
vec_size = 4

context = CKKSContext(poly_modulus_degree, scale, coeff_mod_bit_sizes)
context.generate_keys()
context.print_ckks_params()

m:list[float] = [i+1 for i in range(vec_size)]
t1 = CKKSTensor(context, m * vec_size)  # for rotations we copy the values

matrix = [[float(j+1 + i*vec_size) for j in range(vec_size)] for i in range(vec_size)] # [1,2]

print("A: ",multiply_vector_matrix(m, matrix))
print("B: ")
print_ckks(t1@matrix,vec_size)

