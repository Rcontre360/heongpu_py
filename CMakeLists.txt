cmake_minimum_required(VERSION 3.15)

project(heongpu_py LANGUAGES CXX CUDA)
set(CMAKE_CUDA_ARCHITECTURES 86)
enable_language(CUDA)

find_package(pybind11 CONFIG REQUIRED)
add_subdirectory(packages/HEonGPU)

add_subdirectory(src)

