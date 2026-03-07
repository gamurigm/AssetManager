cmake_minimum_required(VERSION 3.14)
project(CoreEngine LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# ── Include directories ─────────────────────────────────────────────────────
include_directories(include)

# ── Source files ─────────────────────────────────────────────────────────────
set(PORTFOLIO_ENGINE_SOURCES
    src/portfolio_backtest.cpp
)

set(CORE_ENGINE_NATIVE_SOURCES
    src/order_matching.cpp
    src/market_feed.cpp
    src/fix_handler.cpp
)

set(PYBIND_SOURCE src/bindings.cpp)

add_library(portfolio_engine_native STATIC ${PORTFOLIO_ENGINE_SOURCES})
target_include_directories(portfolio_engine_native PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

add_library(core_engine_native STATIC ${CORE_ENGINE_NATIVE_SOURCES})
target_include_directories(core_engine_native PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

# ── Optional: Fix8 library ──────────────────────────────────────────────────
# When Fix8 is installed, set FIX8_ROOT to its prefix (e.g. /usr/local).
# The f8c compiler generates C++ types from fix/schema.xml.
#
#   f8c -Nn ASSETMGR -p AM fix/schema.xml
#
# The generated AM_types.hpp/.cpp and AM_classes.hpp/.cpp must be placed
# in src/ and include/ respectively before enabling HAS_FIX8.

option(USE_FIX8 "Link against the Fix8 FIX engine" OFF)

if(USE_FIX8)
    # --- f8c code generation (run once, or as custom command) ----------------
    find_program(F8C_COMPILER f8c HINTS ${FIX8_ROOT}/bin)
    if(F8C_COMPILER)
        add_custom_command(
            OUTPUT
                ${CMAKE_CURRENT_SOURCE_DIR}/include/AM_types.hpp
                ${CMAKE_CURRENT_SOURCE_DIR}/include/AM_classes.hpp
                ${CMAKE_CURRENT_SOURCE_DIR}/src/AM_types.cpp
                ${CMAKE_CURRENT_SOURCE_DIR}/src/AM_classes.cpp
            COMMAND ${F8C_COMPILER} -Nn ASSETMGR -p AM
                    ${CMAKE_CURRENT_SOURCE_DIR}/fix/schema.xml
            DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/fix/schema.xml
            COMMENT "Generating Fix8 C++ sources from schema.xml"
        )
        target_sources(core_engine_native PRIVATE src/AM_types.cpp src/AM_classes.cpp)
    else()
        message(WARNING "f8c compiler not found – skipping code generation.")
    endif()

    # --- Fix8 runtime library ------------------------------------------------
    find_library(FIX8_LIB fix8 HINTS ${FIX8_ROOT}/lib)
    find_path(FIX8_INCLUDE fix8/f8includes.hpp HINTS ${FIX8_ROOT}/include)

    if(FIX8_LIB AND FIX8_INCLUDE)
        include_directories(${FIX8_INCLUDE})
        add_definitions(-DHAS_FIX8)
        message(STATUS "Fix8 found: ${FIX8_LIB}")
    else()
        message(WARNING "Fix8 library not found – building without FIX support (stub mode).")
    endif()
endif()

if(USE_FIX8 AND FIX8_LIB)
    target_link_libraries(portfolio_engine_native PUBLIC ${FIX8_LIB})
    target_link_libraries(core_engine_native PUBLIC ${FIX8_LIB})
endif()

if(WIN32)
    target_link_libraries(portfolio_engine_native PUBLIC ws2_32)
    target_link_libraries(core_engine_native PUBLIC ws2_32)
endif()

# ── pybind11 (if available) ─────────────────────────────────────────────────
find_package(pybind11 QUIET)
if(pybind11_FOUND)
    pybind11_add_module(core_engine ${PYBIND_SOURCE})
    target_link_libraries(core_engine PRIVATE portfolio_engine_native core_engine_native)
    target_include_directories(core_engine PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)
else()
    message(STATUS "pybind11 not found – skipping Python module and keeping native targets only.")
endif()

add_executable(portfolio_cpp_service src/portfolio_cpp_service.cpp)
target_link_libraries(portfolio_cpp_service PRIVATE portfolio_engine_native)
target_include_directories(portfolio_cpp_service PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)

