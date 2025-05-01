#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "heongpu.cuh"

namespace py = pybind11;

void bind_relinkey(py::module_& m) {
    py::class_<Relinkey>(m, "Relinkey")
        .def(py::init<Parameters&, bool>(),
             py::arg("context"),
             py::arg("store_in_gpu") = true)

        .def(py::init<Parameters&, HostVector<Data64>&, bool>(),
             py::arg("context"),
             py::arg("key"),
             py::arg("store_in_gpu") = true)

        .def(py::init<Parameters&, std::vector<HostVector<Data64>>&, bool>(),
             py::arg("context"),
             py::arg("key"),
             py::arg("store_in_gpu") = true)

        .def("store_in_device",
             [](Relinkey& self, uintptr_t stream) {
                 self.store_in_device(reinterpret_cast<cudaStream_t>(stream));
             },
             py::arg("stream") = 0)

        .def("store_in_host",
             [](Relinkey& self, uintptr_t stream) {
                 self.store_in_host(reinterpret_cast<cudaStream_t>(stream));
             },
             py::arg("stream") = 0)

        .def("is_on_device", &Relinkey::is_on_device)

        .def("data",
             py::overload_cast<>(&Relinkey::data),
             py::return_value_policy::reference_internal)

        .def("data",
             py::overload_cast<size_t>(&Relinkey::data),
             py::arg("i"),
             py::return_value_policy::reference_internal);
}

void bind_galoiskey(py::module_& m) {
    py::class_<Galoiskey>(m, "Galoiskey")
        .def(py::init<Parameters&, bool>(),
             py::arg("context"),
             py::arg("store_in_gpu") = true)

        .def(py::init<Parameters&, std::vector<int>&, bool>(),
             py::arg("context"),
             py::arg("shift_vec"),
             py::arg("store_in_gpu") = true)

        .def(py::init<Parameters&, std::vector<uint32_t>&, bool>(),
             py::arg("context"),
             py::arg("galois_elts"),
             py::arg("store_in_gpu") = true)

        .def("store_in_device",
             [](Galoiskey& self, uintptr_t stream) {
                 self.store_in_device(reinterpret_cast<cudaStream_t>(stream));
             },
             py::arg("stream") = 0)

        .def("store_in_host",
             [](Galoiskey& self, uintptr_t stream) {
                 self.store_in_host(reinterpret_cast<cudaStream_t>(stream));
             },
             py::arg("stream") = 0)

        .def("is_on_device", &Galoiskey::is_on_device)

        .def("data",
             [](Galoiskey& self, size_t i) {
                 return self.data(i);
             },
             py::arg("i"),
             py::return_value_policy::reference_internal)

        .def("c_data",
             [](Galoiskey& self) {
                 return self.c_data();
             },
             py::return_value_policy::reference_internal);
}

void bind_switchkey(py::module_& m) {
    py::class_<Switchkey>(m, "Switchkey")
        .def(py::init<Parameters&, bool>(),
             py::arg("context"),
             py::arg("store_in_gpu") = true)

        .def("store_in_device",
             [](Switchkey& self, uintptr_t stream) {
                 self.store_in_device(reinterpret_cast<cudaStream_t>(stream));
             },
             py::arg("stream") = 0)

        .def("store_in_host",
             [](Switchkey& self, uintptr_t stream) {
                 self.store_in_host(reinterpret_cast<cudaStream_t>(stream));
             },
             py::arg("stream") = 0)

        .def("is_on_device", &Switchkey::is_on_device)

        .def("data",
             [](Switchkey& self) {
                 return self.data();
             },
             py::return_value_policy::reference_internal);
}

void bind_switchkeys(py::module_& m){
    bind_relinkey(m);
    bind_galoiskey(m);
    bind_switchkey(m);
}

