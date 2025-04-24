#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <memory>
#include "heongpu.cuh"

namespace py = pybind11;

void bind_operator(py::module_ &m) {
    py::class_<HEOperator, std::shared_ptr<HEOperator>>(m, "HEOperator")
        .def("add", &HEOperator::add)
        .def("add_inplace", &HEOperator::add_inplace)

        .def("sub", &HEOperator::sub)
        .def("sub_inplace", &HEOperator::sub_inplace)

        .def("negate", &HEOperator::negate)
        .def("negate_inplace", &HEOperator::negate_inplace)

        .def("multiply", &HEOperator::multiply)
        .def("multiply_inplace", &HEOperator::multiply_inplace)

        .def("multiply_plain", &HEOperator::multiply_plain)
        .def("multiply_plain_inplace", &HEOperator::multiply_plain_inplace)

        .def("relinearize_inplace", &HEOperator::relinearize_inplace)

        .def("rotate_rows", &HEOperator::rotate_rows)
        .def("rotate_rows_inplace", &HEOperator::rotate_rows_inplace)

        .def("rotate_columns", &HEOperator::rotate_columns)

        .def("apply_galois", &HEOperator::apply_galois)
        .def("apply_galois_inplace", &HEOperator::apply_galois_inplace)

        .def("keyswitch", &HEOperator::keyswitch)

        .def("conjugate", &HEOperator::conjugate)

        .def("rescale_inplace", &HEOperator::rescale_inplace)

        .def("mod_drop", py::overload_cast<Ciphertext&, Ciphertext&, const ExecutionOptions&>(&HEOperator::mod_drop))
        .def("mod_drop", py::overload_cast<Plaintext&, Plaintext&, const ExecutionOptions&>(&HEOperator::mod_drop))
        .def("mod_drop_inplace", py::overload_cast<Plaintext&, const ExecutionOptions&>(&HEOperator::mod_drop_inplace))
        .def("mod_drop_inplace", py::overload_cast<Ciphertext&, const ExecutionOptions&>(&HEOperator::mod_drop_inplace))

        .def("multiply_power_of_X", &HEOperator::multiply_power_of_X)

        .def("transform_to_ntt", py::overload_cast<Plaintext&, Plaintext&, const ExecutionOptions&>(&HEOperator::transform_to_ntt))
        .def("transform_to_ntt_inplace", py::overload_cast<Plaintext&, const ExecutionOptions&>(&HEOperator::transform_to_ntt_inplace))
        .def("transform_to_ntt", py::overload_cast<Ciphertext&, Ciphertext&, const ExecutionOptions&>(&HEOperator::transform_to_ntt))
        .def("transform_to_ntt_inplace", py::overload_cast<Ciphertext&, const ExecutionOptions&>(&HEOperator::transform_to_ntt_inplace))

        .def("transform_from_ntt", &HEOperator::transform_from_ntt)
        .def("transform_from_ntt_inplace", &HEOperator::transform_from_ntt_inplace);
}

