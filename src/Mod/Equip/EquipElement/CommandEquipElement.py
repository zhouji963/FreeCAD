# ***************************************************************************
# *   Copyright (c) 2023 Ji Qian Zhou <Zhouji963@163.com>                   *
# *                                                                         *
# ***************************************************************************

__title__ = "EquipElement.CommandEquipElement"
__author__ = "Ji Qian Zhou"
__url__ = "http://www.freecad.org"
__doc__ = "EquipElement"


import FreeCAD
from FreeCAD import Qt
import FreeCADGui

import Part
import Equip
from . import EquipElement
from . import ViewProviderEquipElement
import math
import sys


class CommandCylinderShell:
    """Command for creating CylinderShell."""
    def GetResources(self):
        return {'MenuText': Qt.QT_TRANSLATE_NOOP("Equip_CylinderShell","Create CylinderShell"),
                'Accel': "",
                'CmdType': "AlterDoc:Alter3DView:AlterSelection",
                'Pixmap': "EquipElement_CylinderShell",
                'ToolTip': Qt.QT_TRANSLATE_NOOP("Equip_CylinderShell","Creates CylinderShell")}

    def Activated(self):
        text = FreeCAD.Qt.translate("QObject", "Create CylinderShell")
        FreeCAD.ActiveDocument.openTransaction(text)
        CylinderShell = FreeCAD.ActiveDocument.addObject("Part::FeaturePython","CylinderShell")
        EquipElement.CylinderShellFeature(CylinderShell)
        vp = ViewProviderEquipElement.ViewProviderCylinderShell(CylinderShell.ViewObject)
        activePart = FreeCADGui.activeView().getActiveObject('part')
        if activePart:
            activePart.addObject(CylinderShell)
        FreeCAD.ActiveDocument.recompute()
        vp.startDefaultEditMode(CylinderShell.ViewObject)

    def IsActive(self):
        return not FreeCAD.ActiveDocument is None


class CommandSphericalHead:
    """Command for creating SphericalHead."""
    def GetResources(self):
        return {'MenuText': Qt.QT_TRANSLATE_NOOP("Equip_SphericalHead","Create SphericalHead"),
                'Accel': "",
                'CmdType': "AlterDoc:Alter3DView:AlterSelection",
                'Pixmap': "EquipElement_SphericalHead",
                'ToolTip': Qt.QT_TRANSLATE_NOOP("Equip_SphericalHead","Creates SphericalHead")}

    def Activated(self):
        text = FreeCAD.Qt.translate("QObject", "Create SphericalHead")
        FreeCAD.ActiveDocument.openTransaction(text)
        SphericalHead = FreeCAD.ActiveDocument.addObject("Part::FeaturePython","SphericalHead")
        EquipElement.SphericalHeadFeature(SphericalHead)
        vp = ViewProviderEquipElement.ViewProviderSphericalHead(SphericalHead.ViewObject)
        activePart = FreeCADGui.activeView().getActiveObject('part')
        if activePart:
            activePart.addObject(SphericalHead)
        FreeCAD.ActiveDocument.recompute()
        vp.startDefaultEditMode(SphericalHead.ViewObject)

    def IsActive(self):
        return not FreeCAD.ActiveDocument is None

FreeCADGui.addCommand('Equip_CylinderShell', CommandCylinderShell())
FreeCADGui.addCommand('Equip_SphericalHead', CommandSphericalHead())