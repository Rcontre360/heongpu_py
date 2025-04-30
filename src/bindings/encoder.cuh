#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>
#include "heongpu.cuh"

namespace py = pybind11;
using namespace heongpu;

PYBIND11_MAKE_OPAQUE(std::vector<uint64_t>);
PYBIND11_MAKE_OPAQUE(std::vector<int64_t>);
PYBIND11_MAKE_OPAQUE(std::vector<double>);

void bind_encoder(py::module_& m) {
    py::bind_vector<std::vector<uint64_t> >(m, "VecUint");
    py::bind_vector<std::vector<int64_t> >(m, "VecInt");
    py::bind_vector<std::vector<double> >(m, "VecDouble");

    py::class_<HEEncoder>(m, "HEEncoder")
        .def(py::init<Parameters&>(), py::arg("context"))
        .def("encode", py::overload_cast<
            Plaintext&, const std::vector<uint64_t>&, const ExecutionOptions&>(&HEEncoder::encode),
            py::arg("plain"), py::arg("message"), py::arg("options") = ExecutionOptions())
        .def("encode", py::overload_cast<
            Plaintext&, const std::vector<int64_t>&, const ExecutionOptions&>(&HEEncoder::encode),
            py::arg("plain"), py::arg("message"), py::arg("options") = ExecutionOptions())
        .def("encode", py::overload_cast<
            Plaintext&, const HostVector<uint64_t>&, const ExecutionOptions&>(&HEEncoder::encode),
            py::arg("plain"), py::arg("message"), py::arg("options") = ExecutionOptions())
        .def("encode", py::overload_cast<
            Plaintext&, const HostVector<int64_t>&, const ExecutionOptions&>(&HEEncoder::encode),
            py::arg("plain"), py::arg("message"), py::arg("options") = ExecutionOptions())
        .def("encode", py::overload_cast<
            Plaintext&, const std::vector<double>&, double, const ExecutionOptions&>(&HEEncoder::encode),
            py::arg("plain"), py::arg("message"), py::arg("scale"), py::arg("options") = ExecutionOptions())
        .def("encode", py::overload_cast<
            Plaintext&, const HostVector<double>&, double, const ExecutionOptions&>(&HEEncoder::encode),
            py::arg("plain"), py::arg("message"), py::arg("scale"), py::arg("options") = ExecutionOptions())
        //.def("encode", py::overload_cast<
            //Plaintext&, const std::vector<Complex64>&, double, const ExecutionOptions&>(&HEEncoder::encode),
            //py::arg("plain"), py::arg("message"), py::arg("scale"), py::arg("options") = ExecutionOptions())
        //.def("encode", py::overload_cast<
            //Plaintext&, const HostVector<Complex64>&, double, const ExecutionOptions&>(&HEEncoder::encode),
            //py::arg("plain"), py::arg("message"), py::arg("scale"), py::arg("options") = ExecutionOptions())
        .def("encode", py::overload_cast<
            Plaintext&, const double&, double, const ExecutionOptions&>(&HEEncoder::encode),
            py::arg("plain"), py::arg("message"), py::arg("scale"), py::arg("options") = ExecutionOptions())
        .def("encode", py::overload_cast<
            Plaintext&, const std::int64_t&, double, const ExecutionOptions&>(&HEEncoder::encode),
            py::arg("plain"), py::arg("message"), py::arg("scale"), py::arg("options") = ExecutionOptions())

        .def("decode", py::overload_cast<std::vector<uint64_t>&, Plaintext&, const ExecutionOptions&>(&HEEncoder::decode),
            py::arg("message"), py::arg("plain"), py::arg("options") = ExecutionOptions())

        .def("decode", py::overload_cast<std::vector<int64_t>&, Plaintext&, const ExecutionOptions&>(&HEEncoder::decode),
            py::arg("message"), py::arg("plain"), py::arg("options") = ExecutionOptions())

        .def("decode", py::overload_cast<HostVector<uint64_t>&, Plaintext&, const ExecutionOptions&>(&HEEncoder::decode),
            py::arg("message"), py::arg("plain"), py::arg("options") = ExecutionOptions())

        .def("decode", py::overload_cast<HostVector<int64_t>&, Plaintext&, const ExecutionOptions&>(&HEEncoder::decode),
            py::arg("message"), py::arg("plain"), py::arg("options") = ExecutionOptions())

        .def("decode", py::overload_cast<std::vector<double>&, Plaintext&, const ExecutionOptions&>(&HEEncoder::decode),
            py::arg("message"), py::arg("plain"), py::arg("options") = ExecutionOptions())

        .def("decode", py::overload_cast<HostVector<double>&, Plaintext&, const ExecutionOptions&>(&HEEncoder::decode),
            py::arg("message"), py::arg("plain"), py::arg("options") = ExecutionOptions())
        //.def("decode", py::overload_cast<
            //std::vector<Complex64>&, Plaintext&, const ExecutionOptions&>(&HEEncoder::decode),
            //py::arg("message"), py::arg("plain"), py::arg("options") = ExecutionOptions())
        //.def("decode", py::overload_cast<
            //HostVector<Complex64>&, Plaintext&, const ExecutionOptions&>(&HEEncoder::decode),
            //py::arg("message"), py::arg("plain"), py::arg("options") = ExecutionOptions())

        .def("slot_count", &HEEncoder::slot_count);
}

