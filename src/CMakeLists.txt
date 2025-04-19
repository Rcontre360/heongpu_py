# Python module target
cmake_minimum_required(VERSION 3.15...3.26)


pybind11_add_module(heongpu_py MODULE binding.cu)
target_link_libraries(heongpu_py PUBLIC heongpu)
#target_link_libraries(heongpu_py PUBLIC pybind11)

#set_target_properties(heongpu_py PROPERTIES OUTPUT_NAME "heongpu_py")
install(TARGETS heongpu_py DESTINATION .)
