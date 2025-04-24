#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "heongpu.cuh"

namespace py = pybind11;

void bind_public_key(py::module_& m)
{
    using namespace heongpu;

    py::class_<Publickey>(m, "Publickey")
        .def(py::init<>())
        .def(py::init<Parameters&>())
        .def("data", &Publickey::data, py::return_value_policy::reference)

        .def("device_to_host",
             [](Publickey& self, std::vector<Data64>& pk, uintptr_t stream_ptr) {
                 cudaStream_t stream = reinterpret_cast<cudaStream_t>(stream_ptr);
                 self.device_to_host(pk, stream);
             },
             py::arg("public_key"), py::arg("stream_ptr") = 0)

        //.def("device_to_host",
             //[](Publickey& self, HostVector<Data64>& pk, uintptr_t stream_ptr) {
                 //cudaStream_t stream = reinterpret_cast<cudaStream_t>(stream_ptr);
                 //self.device_to_host(pk, stream);
             //},
             //py::arg("public_key"), py::arg("stream_ptr") = 0)

        .def("host_to_device",
             [](Publickey& self, std::vector<Data64>& pk, uintptr_t stream_ptr) {
                 cudaStream_t stream = reinterpret_cast<cudaStream_t>(stream_ptr);
                 self.host_to_device(pk, stream);
             },
             py::arg("public_key"), py::arg("stream_ptr") = 0)

        //.def("host_to_device",
             //[](Publickey& self, HostVector<Data64>& pk, uintptr_t stream_ptr) {
                 //cudaStream_t stream = reinterpret_cast<cudaStream_t>(stream_ptr);
                 //self.host_to_device(pk, stream);
             //},
             //py::arg("public_key"), py::arg("stream_ptr") = 0)

        .def("switch_stream", [](Publickey& self,uintptr_t stream_ptr) {
            self.switch_stream(reinterpret_cast<cudaStream_t>(stream_ptr));
        },py::arg("stream_ptr") = 0)

        .def("stream", [](Publickey& self) {
            return reinterpret_cast<uintptr_t>(self.stream());
        })
        .def("ring_size", &Publickey::ring_size)
        .def("coeff_modulus_count", &Publickey::coeff_modulus_count);

    py::class_<MultipartyPublickey, Publickey>(m, "MultipartyPublickey")
        .def(py::init<Parameters&, RNGSeed>())
        .def("seed", &MultipartyPublickey::seed);
}

