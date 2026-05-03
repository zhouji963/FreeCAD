# ***************************************************************************
# *   Copyright (c) 2023 Ji Qian Zhou <Zhouji963@163.com>                   *
# *                                                                         *
# ***************************************************************************

"""The Equip Workbench GUI initialization."""

import os

import FreeCAD as App
import FreeCADGui as Gui


class EquipWorkbench(Workbench):
    """Equip workbench object."""

    def __init__(self):
        print("Loading Equip workbench...")
        self.__class__.Icon = (
            FreeCAD.getResourceDir() + "Mod/Equip/Resources/icons/EquipWorkbench.svg"
        )
        self.__class__.MenuText = "Equip"
        self.__class__.ToolTip = "Equip workbench: Create Equip with C language"

    def Initialize(self):
        """Initialize the module."""
        print("Initializing Equip workbench...")
        
        # load the builtin modules
        import Equip
        import EquipGui

        try:
            import EquipElement.CommandEquipElement
        except ImportError as err:
            App.Console.PrintError("'EquipElement' package cannot be loaded. "
                                   "{err}\n".format(err=str(err)))

        # from Preferences import preferences


        # build commands list


        print("Equip workbench loaded")

    def Activated(self):
        # update the translation engine
        FreeCADGui.updateLocale()

    def Deactivated(self):
        pass

    def ContextMenu(self, recipient):
        pass

    def GetClassName(self):
        """Type of workbench."""
        return "EquipGui::Workbench"


Gui.addWorkbench(EquipWorkbench())
