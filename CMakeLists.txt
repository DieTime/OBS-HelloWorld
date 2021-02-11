cmake_minimum_required(VERSION 3.13)
project(OBS-HelloWorld)

include(GNUInstallDirs)

set(CMAKE_CXX_STANDARD 11)

add_executable(OBS-HelloWorld main.cpp)

install(TARGETS OBS-HelloWorld RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})