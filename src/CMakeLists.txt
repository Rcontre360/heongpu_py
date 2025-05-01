cmake_minimum_required(VERSION 3.15...3.26)

pybind11_add_module(_heongpu_api MODULE binding.cu)
target_link_libraries(_heongpu_api PRIVATE heongpu cudart)

install(TARGETS _heongpu_api DESTINATION .)
