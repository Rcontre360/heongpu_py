#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "heongpu.cuh"

namespace py = pybind11;
using namespace heongpu;

void bind_decryptor(py::module_& m) {
    py::class_<HEDecryptor>(m, "HEDecryptor")
        .def(py::init<Parameters&, Secretkey&>(), py::arg("context"), py::arg("secret_key"))
        .def("decrypt", &HEDecryptor::decrypt,
             py::arg("plaintext"), py::arg("ciphertext"), py::arg("options") = ExecutionOptions())
        .def("remainder_noise_budget", &HEDecryptor::remainder_noise_budget,
             py::arg("ciphertext"), py::arg("options") = ExecutionOptions())
        //.def("multi_party_decrypt_partial", &HEDecryptor::multi_party_decrypt_partial,
             //py::arg("ciphertext"), py::arg("sk"),
             //py::arg("partial_ciphertext"), py::arg("stream") = cudaStreamDefault)
        .def("multi_party_decrypt_fusion", &HEDecryptor::multi_party_decrypt_fusion,
             py::arg("ciphertexts"), py::arg("plaintext"), py::arg("options") = ExecutionOptions())
        .def("get_seed", &HEDecryptor::get_seed)
        .def("set_seed", &HEDecryptor::set_seed)
        .def("get_offset", &HEDecryptor::get_offset)
        .def("set_offset", &HEDecryptor::set_offset);
}

