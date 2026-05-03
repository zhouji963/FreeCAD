include_directories(
    ${CMAKE_BINARY_DIR}
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_BINARY_DIR}/src
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

include_directories(
    SYSTEM
    ${Boost_INCLUDE_DIRS}
    ${COIN3D_INCLUDE_DIRS}
    ${OCC_INCLUDE_DIR}
    ${PYCXX_INCLUDE_DIR}
    ${Python3_INCLUDE_DIRS}
    ${XercesC_INCLUDE_DIRS}
    ${ZLIB_INCLUDE_DIR}
)

set(EquipGui_LIBS
    Equip
    PartGui
    FreeCADGui
)

set (Equip_TR_QRC ${CMAKE_CURRENT_BINARY_DIR}/Resources/Equip_translation.qrc)
qt_find_and_add_translation(QM_SRCS "Resources/translations/*_*.ts"
    ${CMAKE_CURRENT_BINARY_DIR}/Resources/translations)
qt_create_resource_file(${Equip_TR_QRC} ${QM_SRCS})
qt_add_resources(EquipGui_QRC_SRCS Resources/Equip.qrc ${Equip_TR_QRC})


SET(EquipGui_SRCS
    ${EquipGui_QRC_SRCS}
    ${EquipGui_UIC_HDRS}
    AppEquipGui.cpp
    Command.cpp
    PreCompiled.cpp
    PreCompiled.h
    Workbench.cpp
    Workbench.h
)

SET(EquipGuiIcon_SVG
    Resources/icons/EquipWorkbench.svg
)

add_library(EquipGui SHARED ${EquipGui_SRCS} ${EquipGuiIcon_SVG})

if(FREECAD_USE_PCH)
    target_precompile_headers(EquipGui PRIVATE
            $<$<COMPILE_LANGUAGE:CXX>:"${CMAKE_CURRENT_LIST_DIR}/PreCompiled.h">
    )
endif(FREECAD_USE_PCH)

target_link_libraries(EquipGui ${EquipGui_LIBS})

SET_BIN_DIR(EquipGui EquipGui /Mod/Equip)
SET_PYTHON_PREFIX_SUFFIX(EquipGui)

fc_copy_sources(EquipGui "${CMAKE_BINARY_DIR}/${CMAKE_INSTALL_DATADIR}/Mod/Equip" ${EquipGuiIcon_SVG})

install(TARGETS EquipGui DESTINATION ${CMAKE_INSTALL_LIBDIR})
INSTALL(FILES ${EquipGuiIcon_SVG} DESTINATION "${CMAKE_INSTALL_DATADIR}/Mod/Equip/Resources/icons")

