#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>
#include "./heongpu/api/bindings.cuh"

namespace py = pybind11;

void set_cuda_device(int device_id) {
    HEONGPU_CUDA_CHECK(cudaSetDevice(device_id));
}

int get_device_count() {
    int count;
    HEONGPU_CUDA_CHECK(cudaGetDeviceCount(&count));
    return count;
}

PYBIND11_MODULE(_heongpu_api, m) {
    m.def("set_device", &set_cuda_device, "Set the active CUDA device");
    m.def("get_device_count", &get_device_count, "Get CUDA device count");

    bind_enums(m);
    bind_parameters(m);
    bind_switchkeys(m);
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

