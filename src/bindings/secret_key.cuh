#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "heongpu.cuh"

namespace py = pybind11;
using namespace heongpu;

inline void bind_secret_key(py::module_& m) {
    py::class_<Secretkey>(m, "SecretKey")
        .def(py::init<Parameters&>(), py::arg("context"))
        .def(py::init<Parameters&, int>(), py::arg("context"), py::arg("hamming_weight"))
        .def("ring_size", &Secretkey::ring_size)
        .def("coeff_modulus_count", &Secretkey::coeff_modulus_count)
        .def("switch_stream", [](Secretkey& self,uintptr_t stream_ptr) {
            self.switch_stream(reinterpret_cast<cudaStream_t>(stream_ptr));
        },py::arg("stream_ptr") = 0)
        .def("stream", [](Secretkey& self) {
            return reinterpret_cast<uintptr_t>(self.stream());
        });

}

