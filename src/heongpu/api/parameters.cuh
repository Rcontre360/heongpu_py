#pragma once

#include <pybind11/pybind11.h>
#include "heongpu.cuh"

namespace py = pybind11;
using namespace heongpu;

inline void bind_parameters(py::module_& m) {
    py::class_<Parameters>(m, "Parameters")
        .def(py::init<scheme_type, keyswitching_type, sec_level_type>(),
             py::arg("scheme"),
             py::arg("ks_type"),
             py::arg("sec_level") = sec_level_type::sec128)
        
        // Property accessors
        .def_property_readonly("poly_modulus_degree", &Parameters::poly_modulus_degree)
        .def_property_readonly("log_poly_modulus_degree", &Parameters::log_poly_modulus_degree)
        .def_property_readonly("ciphertext_modulus_count", &Parameters::ciphertext_modulus_count)
        .def_property_readonly("key_modulus_count", &Parameters::key_modulus_count)
        .def_property_readonly("plain_modulus", &Parameters::plain_modulus)
        .def_property_readonly("key_modulus", &Parameters::key_modulus)
        
        // Setters
        .def("set_poly_modulus_degree", &Parameters::set_poly_modulus_degree)
        .def("set_coeff_modulus", &Parameters::set_coeff_modulus)
        .def("set_default_coeff_modulus", &Parameters::set_default_coeff_modulus)
        .def("set_plain_modulus", &Parameters::set_plain_modulus)
        
        // Operations
        .def("generate", &Parameters::generate)
        .def("print_parameters", &Parameters::print_parameters);
}

