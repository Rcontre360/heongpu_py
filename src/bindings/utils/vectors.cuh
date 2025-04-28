#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "heongpu.cuh"

namespace py = pybind11;
using namespace heongpu;

void bind_vectors(py::module_& m) {

    py::class_<DeviceVector<Data64>>(m, "DeviceVector")
        .def(py::init<>())
        .def(py::init([](size_t size, uintptr_t stream_ptr) {
            cudaStream_t stream = reinterpret_cast<cudaStream_t>(stream_ptr);
            return std::make_unique<DeviceVector<Data64>>(size, stream, MemoryPool::instance().get_device_resource());
            //return DeviceVector<Data64>(size, stream, MemoryPool::instance().get_device_resource());
        }), py::arg("size"), py::arg("stream_ptr") = 0)
        .def(py::init([](const std::vector<Data64>& v, uintptr_t stream_ptr) {
            cudaStream_t stream = reinterpret_cast<cudaStream_t>(stream_ptr);
            return std::make_unique<DeviceVector<Data64>>(v, stream, MemoryPool::instance().get_device_resource());
            //return DeviceVector<Data64>(v, stream, MemoryPool::instance().get_device_resource());
        }), py::arg("vector"), py::arg("stream_ptr") = 0)
        .def("__len__", [](const DeviceVector<Data64>& vec) {
            return vec.size();
        })
        .def("__getitem__", [](const DeviceVector<Data64>& vec, size_t i) {
            throw py::type_error("DeviceVector elements must be copied to host for access.");
        })
        .def("__setitem__", [](DeviceVector<Data64>& vec, size_t i, Data64) {
            throw py::type_error("DeviceVector elements cannot be modified directly from Python.");
        })
        .def("resize", [](DeviceVector<Data64>& vec, size_t new_size, uintptr_t stream_ptr) {
            cudaStream_t stream = reinterpret_cast<cudaStream_t>(stream_ptr);
            vec.resize(new_size, stream);
        }, py::arg("new_size"), py::arg("stream_ptr") = 0)
        .def("reserve", [](DeviceVector<Data64>& vec, size_t new_size, uintptr_t stream_ptr) {
            cudaStream_t stream = reinterpret_cast<cudaStream_t>(stream_ptr);
            vec.reserve(new_size, stream);
        }, py::arg("new_size"), py::arg("stream_ptr") = 0)
        .def("append", [](DeviceVector<Data64>& vec, const DeviceVector<Data64>& other, uintptr_t stream_ptr) {
            cudaStream_t stream = reinterpret_cast<cudaStream_t>(stream_ptr);
            vec.append(other, stream);
        }, py::arg("other"), py::arg("stream_ptr") = 0)
        .def("data", [](DeviceVector<Data64>& vec) {
            return reinterpret_cast<uintptr_t>(vec.data());
        });

    py::class_<HostVector<Data64>>(m, "HostVector")
        .def(py::init<>())
        .def("__len__", [](const HostVector<Data64>& vec) {
            return vec.size();
        })
        .def("__getitem__", [](const HostVector<Data64>& vec, size_t i) {
            if (i >= vec.size()) throw py::index_error();
            return vec[i];
        })
        .def("__setitem__", [](HostVector<Data64>& vec, size_t i, Data64 value) {
            if (i >= vec.size()) throw py::index_error();
            vec[i] = value;
        })
        .def("resize", [](HostVector<Data64>& vec, size_t new_size) {
            vec.resize(new_size);
        })
        .def("get", [](const HostVector<Data64>& vec, size_t i) {
            if (i >= vec.size()) throw py::index_error();
            return vec[i];
        }, py::arg("index"));

}

