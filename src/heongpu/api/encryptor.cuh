#include <pybind11/pybind11.h>
#include "heongpu.cuh"

namespace py = pybind11;
using namespace heongpu;

void bind_encryptor(py::module_& m) {
    py::class_<HEEncryptor>(m, "HEEncryptor")
        .def(py::init<Parameters&, Publickey&>(), py::arg("context"), py::arg("public_key"))
        .def("encrypt", &HEEncryptor::encrypt,
             py::arg("ciphertext"), py::arg("plaintext"), py::arg("options") = ExecutionOptions())
        .def("get_seed", &HEEncryptor::get_seed)
        .def("set_seed", &HEEncryptor::set_seed)
        .def("get_offset", &HEEncryptor::get_offset)
        .def("set_offset", &HEEncryptor::set_offset);
}

