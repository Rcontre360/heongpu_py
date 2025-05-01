#include <pybind11/pybind11.h>
#include "heongpu.cuh"

namespace py = pybind11;
using namespace heongpu;

void bind_storagemanager(py::module_& m) {

    py::class_<ExecutionOptions>(m, "ExecutionOptions")
        .def(py::init<>())
        .def_property("stream",
            [](const ExecutionOptions& opts) {
                return reinterpret_cast<uintptr_t>(opts.stream_);
            },
            [](ExecutionOptions& opts, uintptr_t stream_ptr) {
                opts.stream_ = reinterpret_cast<cudaStream_t>(stream_ptr);
            },
            "CUDA stream to be used for execution.")
        .def_property("storage",
            [](const ExecutionOptions& opts) {
                return opts.storage_;
            },
            [](ExecutionOptions& opts, storage_type storage) {
                opts.storage_ = storage;
            },
            "Storage type to use (DEVICE or HOST).")
        .def_property("keep_initial_condition",
            [](const ExecutionOptions& opts) {
                return opts.keep_initial_condition_;
            },
            [](ExecutionOptions& opts, bool value) {
                opts.keep_initial_condition_ = value;
            },
            "Whether to maintain initial data location.")
        .def("set_stream", [](ExecutionOptions& opts, uintptr_t stream_ptr) {
            return opts.set_stream(reinterpret_cast<cudaStream_t>(stream_ptr));
        }, py::arg("stream_ptr"), py::return_value_policy::reference_internal)
        .def("set_storage_type", &ExecutionOptions::set_storage_type,
             py::arg("storage"), py::return_value_policy::reference_internal)
        .def("set_initial_location", &ExecutionOptions::set_initial_location,
             py::arg("keep_initial_condition"), py::return_value_policy::reference_internal);

}

