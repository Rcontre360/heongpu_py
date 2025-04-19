#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>
#include "heongpu.cuh"

namespace py = pybind11;
using namespace heongpu;


PYBIND11_MODULE(heongpu_py, m) {
    // Enum bindings
    py::enum_<scheme_type>(m, "SchemeType")
        .value("BFV", scheme_type::bfv)
        .value("BGV", scheme_type::bgv)
        .value("CKKS", scheme_type::ckks)
        .export_values();

    py::enum_<keyswitching_type>(m, "KeySwitchingType")
        .value("NONE", keyswitching_type::NONE)
        .value("METHOD_I", keyswitching_type::KEYSWITCHING_METHOD_I)
        .value("METHOD_II", keyswitching_type::KEYSWITCHING_METHOD_II)
        .value("METHOD_III", keyswitching_type::KEYSWITCHING_METHOD_III)
        .export_values();

    py::enum_<sec_level_type>(m, "SecurityLevel")
        .value("SEC128", sec_level_type::sec128)
        .value("SEC192", sec_level_type::sec192)
        .value("SEC256", sec_level_type::sec256)
        .export_values();

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
        .def("set_custom_coeff_modulus", &Parameters::set_custom_coeff_modulus)
        .def("set_default_coeff_modulus", &Parameters::set_default_coeff_modulus)
        .def("set_plain_modulus", &Parameters::set_plain_modulus)
        
        // Operations
        .def("generate", &Parameters::generate)
        .def("print_parameters", &Parameters::print_parameters);


    //py::class_<Secretkey>(m, "SecretKey")
        //.def(py::init<const Parameters&>());

    //py::class_<Publickey>(m, "PublicKey")
        //.def(py::init<const Parameters&>());

    //py::class_<HEKeyGenerator>(m, "HEKeyGenerator")
        //.def(py::init<const Parameters&>())
        //.def("generate_secret_key", &HEKeyGenerator::generate_secret_key)
        //.def("generate_public_key", &HEKeyGenerator::generate_public_key);

    //py::class_<HEEncoder>(m, "HEEncoder")
        //.def(py::init<const Parameters&>())
        //.def("encode", &HEEncoder::encode)
        //.def("decode", &HEEncoder::decode);

    //py::class_<HEEncryptor>(m, "HEEncryptor")
        //.def(py::init<const Parameters&, const Publickey&>())
        //.def("encrypt", &HEEncryptor::encrypt);

    //py::class_<HEDecryptor>(m, "HEDecryptor")
        //.def(py::init<const Parameters&, const Secretkey&>())
        //.def("decrypt", &HEDecryptor::decrypt);

    //py::class_<HEOperator>(m, "HEOperator")
        //.def(py::init<const Parameters&>())
        //.def("add_inplace", &HEOperator::add_inplace);

    //py::class_<Plaintext>(m, "Plaintext")
        //.def(py::init<const Parameters&>());

    //py::class_<Ciphertext>(m, "Ciphertext")
        //.def(py::init<const Parameters&>());
}

