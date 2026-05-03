# ***************************************************************************
# *   Copyright (c) 2023 Ji Qian Zhou <Zhouji963@163.com>                   *
# *                                                                         *
# ***************************************************************************

__title__ = "EquipElement.ViewProviderEquipElement"
__author__ = "Ji Qian Zhou"
__url__ = "http://www.freecad.org"
__doc__ = "EquipElement"


import os
import FreeCAD
import FreeCADGui

from PySide import QtGui


class ViewProviderCylinderShell:
    def __init__(self, viewObject):
        ''' Set this object to the proxy object of the actual view provider '''
        viewObject.Proxy = self
        viewObject.addExtension("PartGui::ViewProviderAttachExtensionPython")
        viewObject.setIgnoreOverlayIcon(True, "PartGui::ViewProviderAttachExtensionPython")

    def attach(self, viewObject):
        ''' Setup the scene sub-graph of the view provider, this method is mandatory '''
        return

    def setupContextMenu(self, viewObject, menu):
        action = menu.addAction(FreeCAD.Qt.translate("QObject", "Edit %1").replace("%1", viewObject.Object.Label))
        action.triggered.connect(lambda: self.startDefaultEditMode(viewObject))
        return False

    def startDefaultEditMode(self, viewObject):
        document = viewObject.Document.Document
        if not document.HasPendingTransaction:
            text = FreeCAD.Qt.translate("QObject", "Edit %1").replace("%1", viewObject.Object.Label)
            document.openTransaction(text)
        viewObject.Document.setEdit(viewObject.Object, 0)

    def setEdit(self, viewObject, mode):
        if mode == 0:
            FreeCADGui.Control.showDialog(TaskCylinderShellUI(viewObject))
            return True

    def unsetEdit(self, viewObject, mode):
        if mode == 0:
            FreeCADGui.Control.closeDialog()
            return True

    def getIcon(self):
        return ":/icons/EquipElement_CylinderShell.svg"

    def dumps(self):
        return None

    def loads(self,state):
        return None



class TaskCylinderShellUI:
    """A default task panel for editing CylinderShell objects."""

    def __init__(self, viewObject):
        self.viewObject = viewObject
        ui_file = os.path.join(os.path.dirname(__file__), "EquipElement_CylinderShell_Task.ui")
        ui = FreeCADGui.UiLoader()
        self.form = ui.load(ui_file)

        object = self.viewObject.Object
        self.form.CylinderShellOuterDiameter.setProperty("rawValue", object.OuterDiameter.Value)
        self.form.CylinderShellInnerDiameter.setProperty("rawValue", object.InnerDiameter.Value)
        self.form.CylinderShellHeight.setProperty("rawValue", object.Height.Value)

        self.form.CylinderShellOuterDiameter.valueChanged.connect(lambda x: self.onChangeOuterDiameter(x))
        self.form.CylinderShellInnerDiameter.valueChanged.connect(lambda x: self.onChangeInnerDiameter(x))
        self.form.CylinderShellHeight.valueChanged.connect(lambda x: self.onChangeHeight(x))

        FreeCADGui.ExpressionBinding(self.form.CylinderShellOuterDiameter).bind(object,"OuterDiameter")
        FreeCADGui.ExpressionBinding(self.form.CylinderShellInnerDiameter).bind(object,"InnerDiameter")
        FreeCADGui.ExpressionBinding(self.form.CylinderShellHeight).bind(object,"Height")

    def onChangeOuterDiameter(self, diameter):
        object = self.viewObject.Object
        object.OuterDiameter = diameter
        object.recompute()

    def onChangeInnerDiameter(self, diameter):
        object = self.viewObject.Object
        object.InnerDiameter = diameter
        object.recompute()

    def onChangeHeight(self, height):
        object = self.viewObject.Object
        object.Height = height
        object.recompute()

    def accept(self):
        object = self.viewObject.Object
        if not object.isValid():
            QtGui.QMessageBox.warning(None, "Error", object.getStatusString())
            return False
        document = self.viewObject.Document.Document
        document.commitTransaction()
        document.recompute()
        self.viewObject.Document.resetEdit()
        return True

    def reject(self):
        guidocument = self.viewObject.Document
        document = guidocument.Document
        document.abortTransaction()
        document.recompute()
        guidocument.resetEdit()
        return True


class ViewProviderSphericalHead:
    def __init__(self, obj):
        ''' Set this object to the proxy object of the actual view provider '''
        obj.Proxy = self
        obj.addExtension("PartGui::ViewProviderAttachExtensionPython")
        obj.setIgnoreOverlayIcon(True, "PartGui::ViewProviderAttachExtensionPython")

    def attach(self, obj):
        ''' Setup the scene sub-graph of the view provider, this method is mandatory '''
        return

    def setupContextMenu(self, viewObject, menu):
        action = menu.addAction(FreeCAD.Qt.translate("QObject", "Edit %1").replace("%1", viewObject.Object.Label))
        action.triggered.connect(lambda: self.startDefaultEditMode(viewObject))
        return False

    def startDefaultEditMode(self, viewObject):
        document = viewObject.Document.Document
        if not document.HasPendingTransaction:
            text = FreeCAD.Qt.translate("QObject", "Edit %1").replace("%1", viewObject.Object.Label)
            document.openTransaction(text)
        viewObject.Document.setEdit(viewObject.Object, 0)

    def setEdit(self, viewObject, mode):
        if mode == 0:
            FreeCADGui.Control.showDialog(TaskSphericalHeadUI(viewObject))
            return True

    def unsetEdit(self, viewObject, mode):
        if mode == 0:
            FreeCADGui.Control.closeDialog()
            return True

    def getIcon(self):
        return ":/icons/EquipElement_SphericalHead.svg"

    def __getstate__(self):
        return None

    def __setstate__(self,state):
        return None


class TaskSphericalHeadUI:
    """A default task panel for editing SphericalHead objects."""

    def __init__(self, viewObject):
        self.viewObject = viewObject
        ui_file = os.path.join(os.path.dirname(__file__), "EquipElement_SphericalHead_Task.ui")
        ui = FreeCADGui.UiLoader()
        self.form = ui.load(ui_file)

        object = self.viewObject.Object
        self.form.SphericalHeadOuterDiameter.setProperty("rawValue", object.OuterDiameter.Value)
        self.form.SphericalHeadInnerDiameter.setProperty("rawValue", object.InnerDiameter.Value)


        self.form.SphericalHeadOuterDiameter.valueChanged.connect(lambda x: self.onChangeOuterDiameter(x))
        self.form.SphericalHeadInnerDiameter.valueChanged.connect(lambda x: self.onChangeInnerDiameter(x))


        FreeCADGui.ExpressionBinding(self.form.SphericalHeadOuterDiameter).bind(object,"OuterDiameter")
        FreeCADGui.ExpressionBinding(self.form.SphericalHeadInnerDiameter).bind(object,"InnerDiameter")


    def onChangeOuterDiameter(self, diameter):
        object = self.viewObject.Object
        object.OuterDiameter = diameter
        object.recompute()

    def onChangeInnerDiameter(self, diameter):
        object = self.viewObject.Object
        object.InnerDiameter = diameter
        object.recompute()


    def accept(self):
        object = self.viewObject.Object
        if not object.isValid():
            QtGui.QMessageBox.warning(None, "Error", object.getStatusString())
            return False
        document = self.viewObject.Document.Document
        document.commitTransaction()
        document.recompute()
        self.viewObject.Document.resetEdit()
        return True

    def reject(self):
        guidocument = self.viewObject.Document
        document = guidocument.Document
        document.abortTransaction()
        document.recompute()
        guidocument.resetEdit()
        return True