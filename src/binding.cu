#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>
#include "./bindings/bindings.cuh"

namespace py = pybind11;

PYBIND11_MODULE(heongpu_py, m) {
    bind_enums(m);
    bind_parameters(m);
    bind_public_key(m);
    bind_secret_key(m);
    bind_hekey_generator(m);
    bind_vectors(m);
    bind_storagemanager(m);
    bind_plaintext(m);
    bind_encoder(m);
    bind_encryptor(m);
    bind_decryptor(m);
    bind_operator(m);
    bind_ciphertext(m);
}

