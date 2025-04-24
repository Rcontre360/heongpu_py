#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <cstdint>  // for uintptr_t
#include <vector>
#include "heongpu.cuh"

namespace py = pybind11;
using namespace heongpu;

void bind_hekey_generator(py::module_& m) {
    py::class_<HEKeyGenerator>(m, "HEKeyGenerator")
        .def(py::init<Parameters&>(), py::arg("context"))

        .def("generate_secret_key", [](HEKeyGenerator& self, Secretkey& sk, uintptr_t stream_ptr) {
            self.generate_secret_key(sk, reinterpret_cast<cudaStream_t>(stream_ptr));
        }, py::arg("sk"), py::arg("stream_ptr") = 0)

        .def("generate_public_key", [](HEKeyGenerator& self, Publickey& pk, Secretkey& sk, uintptr_t stream_ptr) {
            self.generate_public_key(pk, sk, reinterpret_cast<cudaStream_t>(stream_ptr));
        }, py::arg("pk"), py::arg("sk"), py::arg("stream_ptr") = 0)

        //.def("generate_multi_party_public_key_piece", [](HEKeyGenerator& self, Publickey& pk, Secretkey& sk, uintptr_t stream_ptr) {
            //self.generate_multi_party_public_key_piece(pk, sk, reinterpret_cast<cudaStream_t>(stream_ptr));
        //}, py::arg("pk"), py::arg("sk"), py::arg("stream_ptr") = 0)

        //.def("generate_multi_party_public_key", [](HEKeyGenerator& self, std::vector<Publickey>& all_pk, Publickey& pk, uintptr_t stream_ptr) {
            //self.generate_multi_party_public_key(all_pk, pk, reinterpret_cast<cudaStream_t>(stream_ptr));
        //}, py::arg("all_pk"), py::arg("pk"), py::arg("stream_ptr") = 0)

        //.def("generate_relin_key", [](HEKeyGenerator& self, Relinkey& rk, Secretkey& sk, uintptr_t stream_ptr) {
            //self.generate_relin_key(rk, sk, reinterpret_cast<cudaStream_t>(stream_ptr));
        //}, py::arg("rk"), py::arg("sk"), py::arg("stream_ptr") = 0)

        //.def("generate_multi_party_relin_key_piece", [](HEKeyGenerator& self, MultipartyRelinkey& rk, Secretkey& sk, uintptr_t stream_ptr) {
            //self.generate_multi_party_relin_key_piece(rk, sk, reinterpret_cast<cudaStream_t>(stream_ptr));
        //}, py::arg("rk"), py::arg("sk"), py::arg("stream_ptr") = 0)

        //.def("generate_multi_party_relin_key_piece", [](HEKeyGenerator& self, MultipartyRelinkey& rk_s1_common, MultipartyRelinkey& rk_new, Secretkey& sk, uintptr_t stream_ptr) {
            //self.generate_multi_party_relin_key_piece(rk_s1_common, rk_new, sk, reinterpret_cast<cudaStream_t>(stream_ptr));
        //}, py::arg("rk_s1_common"), py::arg("rk_new"), py::arg("sk"), py::arg("stream_ptr") = 0)

        //.def("generate_galois_key", [](HEKeyGenerator& self, Galoiskey& gk, Secretkey& sk, uintptr_t stream_ptr) {
            //self.generate_galois_key(gk, sk, reinterpret_cast<cudaStream_t>(stream_ptr));
        //}, py::arg("gk"), py::arg("sk"), py::arg("stream_ptr") = 0)

        //.def("generate_multi_party_galios_key_piece", [](HEKeyGenerator& self, Galoiskey& gk, Secretkey& sk, uintptr_t stream_ptr) {
            //self.generate_multi_party_galios_key_piece(gk, sk, reinterpret_cast<cudaStream_t>(stream_ptr));
        //}, py::arg("gk"), py::arg("sk"), py::arg("stream_ptr") = 0)

        //.def("generate_multi_party_galois_key", [](HEKeyGenerator& self, std::vector<Galoiskey>& all_gk, Galoiskey& gk, uintptr_t stream_ptr) {
            //self.generate_multi_party_galois_key(all_gk, gk, reinterpret_cast<cudaStream_t>(stream_ptr));
        //}, py::arg("all_gk"), py::arg("gk"), py::arg("stream_ptr") = 0)

        .def("generate_switch_key", [](HEKeyGenerator& self, Switchkey& swk, Secretkey& new_sk, Secretkey& old_sk, uintptr_t stream_ptr) {
            self.generate_switch_key(swk, new_sk, old_sk, reinterpret_cast<cudaStream_t>(stream_ptr));
        }, py::arg("swk"), py::arg("new_sk"), py::arg("old_sk"), py::arg("stream_ptr") = 0)

        .def("get_seed", &HEKeyGenerator::get_seed)
        .def("set_seed", &HEKeyGenerator::set_seed)
        .def("get_offset", &HEKeyGenerator::get_offset)
        .def("set_offset", &HEKeyGenerator::set_offset);
}

