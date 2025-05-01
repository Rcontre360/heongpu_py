#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <pybind11/functional.h>
#include "heongpu.cuh"

namespace py = pybind11;
using namespace heongpu;

void bind_ciphertext(py::module_& m) {
    py::class_<Ciphertext>(m, "Ciphertext")
    .def(py::init<>())
    .def(py::init<Parameters&, const ExecutionOptions&>(),
         py::arg("context"), py::arg("options") = ExecutionOptions())
    .def(py::init<const std::vector<Data64>&, Parameters&, const ExecutionOptions&>(),
         py::arg("cipher"), py::arg("context"), py::arg("options") = ExecutionOptions())
    .def(py::init<const HostVector<Data64>&, Parameters&, const ExecutionOptions&>(),
         py::arg("cipher"), py::arg("context"), py::arg("options") = ExecutionOptions())

    .def("store_in_device", [](Ciphertext& self, uintptr_t stream_ptr) {
        self.store_in_device(reinterpret_cast<cudaStream_t>(stream_ptr));
    }, py::arg("stream_ptr") = 0)

    .def("store_in_host", [](Ciphertext& self, uintptr_t stream_ptr) {
        self.store_in_host(reinterpret_cast<cudaStream_t>(stream_ptr));
    }, py::arg("stream_ptr") = 0)

    .def("is_on_device", &Ciphertext::is_on_device)

    .def("data", &Ciphertext::data, py::return_value_policy::reference)

    .def("get_data", [](Ciphertext& self, std::vector<Data64>& cipher, uintptr_t stream_ptr) {
        self.get_data(cipher, reinterpret_cast<cudaStream_t>(stream_ptr));
    }, py::arg("cipher"), py::arg("stream_ptr") = 0)

    .def("get_data_host", [](Ciphertext& self, HostVector<Data64>& cipher, uintptr_t stream_ptr) {
        self.get_data(cipher, reinterpret_cast<cudaStream_t>(stream_ptr));
    }, py::arg("cipher"), py::arg("stream_ptr") = 0)

    .def("switch_stream", [](Ciphertext& self, uintptr_t stream_ptr) {
        self.switch_stream(reinterpret_cast<cudaStream_t>(stream_ptr));
    }, py::arg("stream_ptr"))

    .def("stream", [](const Ciphertext& self) -> uintptr_t {
        return reinterpret_cast<uintptr_t>(self.stream());
    })

    .def("ring_size", &Ciphertext::ring_size)
    .def("coeff_modulus_count", &Ciphertext::coeff_modulus_count)
    .def("size", &Ciphertext::size)
    .def("depth", &Ciphertext::depth)
    .def("in_ntt_domain", &Ciphertext::in_ntt_domain)
    .def("scale", &Ciphertext::scale)
    .def("rescale_required", &Ciphertext::rescale_required)
    .def("relinearization_required", &Ciphertext::relinearization_required)
    .def(py::init<const Ciphertext&>());  // copy constructor
    //.def("copy_assign", [](Ciphertext& self, const Ciphertext& other) {
        //self = other;
        //return self;
     //})
    //.def("move_assign", [](Ciphertext& self, Ciphertext& other) {
        //self = std::move(other);
        //return self;
    //});
}

