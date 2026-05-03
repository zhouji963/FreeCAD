
add_subdirectory(App)
if(BUILD_GUI)
    add_subdirectory(Gui)
endif(BUILD_GUI)

set(Equip_Scripts
    Init.py
)

if(BUILD_GUI)
    list (APPEND Equip_Scripts InitGui.py)
endif(BUILD_GUI)

set(EquipElement_Scripts
    EquipElement/__init__.py
    EquipElement/EquipElement.py
)

if(BUILD_GUI)
    list (APPEND EquipElement_Scripts
          EquipElement/CommandEquipElement.py
          EquipElement/ViewProviderEquipElement.py
          EquipElement/EquipElement_CylinderShell_Task.ui
	      EquipElement/EquipElement_SphericalHead_Task.ui
    )
endif(BUILD_GUI)

add_custom_target(EquipScripts ALL SOURCES 
    ${Equip_Scripts}
    ${EquipElement_Scripts}   
)

fc_target_copy_resource(EquipScripts
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_BINARY_DIR}/Mod/Equip
    ${Equip_Scripts}
    ${EquipElement_Scripts}   
)

install(
    FILES
        ${Equip_Scripts}
    DESTINATION
        Mod/Equip
)

INSTALL(
    FILES
        ${EquipElement_Scripts}
    DESTINATION
        Mod/Equip/EquipElement
)
