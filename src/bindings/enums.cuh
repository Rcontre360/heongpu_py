#pragma once

#include <pybind11/pybind11.h>
#include "heongpu.cuh"

namespace py = pybind11;
using namespace heongpu;

inline void bind_enums(py::module_& m) {
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
}

