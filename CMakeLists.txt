cmake_minimum_required(VERSION 3.15)

project(heongpu_py LANGUAGES CXX CUDA)
set(CMAKE_CUDA_ARCHITECTURES 86)
set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} --use_fast_math")
enable_language(CUDA)

find_package(pybind11 CONFIG REQUIRED)
add_subdirectory(packages/HEonGPU)

add_subdirectory(src)

