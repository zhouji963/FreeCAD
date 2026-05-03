include_directories(
  ${CMAKE_BINARY_DIR}
  ${CMAKE_BINARY_DIR}/src
  ${CMAKE_SOURCE_DIR}/src
  ${CMAKE_CURRENT_BINARY_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}
)

include_directories(
  SYSTEM
  ${Boost_INCLUDE_DIRS}
  ${OCC_INCLUDE_DIR}
  ${PYCXX_INCLUDE_DIR}
  ${Python3_INCLUDE_DIRS}
  ${ZLIB_INCLUDE_DIR}
  ${XercesC_INCLUDE_DIRS}
  ${FREETYPE_INCLUDE_DIRS}
)

link_directories(${OCC_LIBRARY_DIR})

set(Equip_LIBS
  FreeCADApp
  Part
)

SET(Equip_SRCS
  AppEquip.cpp
  PreCompiled.cpp
  PreCompiled.h
)

add_library(Equip SHARED ${Equip_SRCS})

if(FREECAD_USE_PCH)
    target_precompile_headers(Equip PRIVATE
            $<$<COMPILE_LANGUAGE:CXX>:"${CMAKE_CURRENT_LIST_DIR}/PreCompiled.h">
    )
endif(FREECAD_USE_PCH)

target_link_libraries(Equip ${Equip_LIBS})

SET_BIN_DIR(Equip Equip /Mod/Equip)
SET_PYTHON_PREFIX_SUFFIX(Equip)

install(TARGETS Equip DESTINATION ${CMAKE_INSTALL_LIBDIR})
