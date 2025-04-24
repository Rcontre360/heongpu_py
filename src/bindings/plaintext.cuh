#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "heongpu.cuh"

namespace py = pybind11;
using namespace heongpu;

void bind_plaintext(py::module_& m) {
    py::class_<Plaintext>(m, "Plaintext")
        .def(py::init<>())
        .def(py::init<Parameters&, const ExecutionOptions&>(),
             py::arg("context"), py::arg("options") = ExecutionOptions())
        .def(py::init<const std::vector<Data64>&, Parameters&, const ExecutionOptions&>(),
             py::arg("plain"), py::arg("context"), py::arg("options") = ExecutionOptions())
        .def(py::init<const HostVector<Data64>&, Parameters&, const ExecutionOptions&>(),
             py::arg("plain"), py::arg("context"), py::arg("options") = ExecutionOptions())
        .def("store_in_device", [](Plaintext& self, uintptr_t stream_ptr) {
            self.store_in_device(reinterpret_cast<cudaStream_t>(stream_ptr));
        }, py::arg("stream_ptr") = 0)
        .def("store_in_host", [](Plaintext& self, uintptr_t stream_ptr) {
            self.store_in_host(reinterpret_cast<cudaStream_t>(stream_ptr));
        }, py::arg("stream_ptr") = 0)
        .def("is_on_device", &Plaintext::is_on_device)
        .def("get_data_vector", [](Plaintext& self, uintptr_t stream_ptr) {
            std::vector<Data64> data;
            self.get_data(data, reinterpret_cast<cudaStream_t>(stream_ptr));
            return data;
        }, py::arg("stream_ptr") = 0)
        .def("set_data_vector", [](Plaintext& self, const std::vector<Data64>& data) {
            self.set_data(data);
        }, py::arg("data"))
        .def("get_data_host_vector", [](Plaintext& self, uintptr_t stream_ptr) {
            HostVector<Data64> data;
            self.get_data(data, reinterpret_cast<cudaStream_t>(stream_ptr));
            return data;
        }, py::arg("stream_ptr") = 0)
        .def("set_data_host_vector", [](Plaintext& self, const HostVector<Data64>& data) {
            self.set_data(data);
        }, py::arg("data"))
        .def("size", &Plaintext::size)
        .def("depth", &Plaintext::depth)
        .def("scale", &Plaintext::scale)
        .def("in_ntt_domain", &Plaintext::in_ntt_domain);
}

