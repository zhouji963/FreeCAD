# ***************************************************************************
# *   Copyright (c) 2023 Ji Qian Zhou <Zhouji963@163.com>                   *
# *                                                                         *
# ***************************************************************************

__title__ = "EquipElement.FeatureEquipElement"
__author__ = "Ji Qian Zhou"
__url__ = "http://www.freecad.org"
__doc__ = "EquipElement"


import FreeCAD
import Part
import Equip


def makeCylinderShell(outerDiameter, innerDiameter, height):
    outer_cylinder = Part.makeCylinder(outerDiameter/2, height)
    shape = outer_cylinder
    if innerDiameter > 0 and innerDiameter < outerDiameter:
        inner_cylinder = Part.makeCylinder(innerDiameter/2, height)
        shape = outer_cylinder.cut(inner_cylinder)
    return shape


class CylinderShellFeature:
    def __init__(self, obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyLength","Height","CylinderShell", "Height of the CylinderShell").Height = 5000.0
        obj.addProperty("App::PropertyLength","InnerDiameter","CylinderShell","Inner Diameter").InnerDiameter = 1000.0
        obj.addProperty("App::PropertyLength","OuterDiameter","CylinderShell","Outer Diameter").OuterDiameter = 1040.0
        obj.addExtension("Part::AttachExtensionPython")

    def execute(self, fp):
        if fp.InnerDiameter >= fp.OuterDiameter:
            raise ValueError("Inner Diameter must be smaller than outer Diameter")
        fp.Shape = makeCylinderShell(fp.OuterDiameter, fp.InnerDiameter, fp.Height)


def addCylinderShell(doc, name="CylinderShell"):
    """addCylinderShell(document, [name]): adds a CylinderShell object"""

    obj = doc.addObject("Part::FeaturePython", name)
    CylinderShellFeature(obj)
    if FreeCAD.GuiUp:
        from . import ViewProviderEquipElement
        ViewProviderEquipElement.ViewProviderCylinderShell(obj.ViewObject)
    return obj


def makeSphericalHead(outerDiameter, innerDiameter):
    outer_HemiSphere = Part.makeSphere(outerDiameter/2, FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), -90, 0, 360)
    shape = outer_HemiSphere
    if innerDiameter > 0 and innerDiameter < outerDiameter:
        inner_HemiSphere = Part.makeSphere(innerDiameter/2, FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), -90, 0, 360)
        shape = outer_HemiSphere.cut(inner_HemiSphere)
    return shape


class SphericalHeadFeature:
    def __init__(self, obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyLength","InnerDiameter","SphericalHead","Inner Diameter").InnerDiameter = 1000.0
        obj.addProperty("App::PropertyLength","OuterDiameter","SphericalHead","Outer Diameter").OuterDiameter = 1040.0
        obj.addExtension("Part::AttachExtensionPython")

    def execute(self, fp):
        if fp.InnerDiameter >= fp.OuterDiameter:
            raise ValueError("Inner Diameter must be smaller than outer Diameter")
        fp.Shape = makeSphericalHead(fp.OuterDiameter, fp.InnerDiameter)


def addSphericalHead(doc, name="SphericalHead"):
    """addSphericalHead(document, [name]): adds a SphericalHead object"""

    obj = doc.addObject("Part::FeaturePython", name)
    SphericalHeadFeature(obj)
    if FreeCAD.GuiUp:
        from . import ViewProviderEquipElement
        ViewProviderEquipElement.ViewProviderSphericalHead(obj.ViewObject)
    return obj