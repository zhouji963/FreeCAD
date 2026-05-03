/***************************************************************************
 *   Copyright (c) 2023 Ji Qian Zhou <Zhouji963@163.com>                   *
 *                                                                         *
 ***************************************************************************/

#include "PreCompiled.h"

#include <Base/Console.h>
#include <Base/Interpreter.h>
#include <Base/PyObjectBase.h>
#include <Gui/Application.h>

#include "Workbench.h"


// use a different name to CreateCommand()
void CreateEquipCommands();


namespace EquipGui {
class Module : public Py::ExtensionModule<Module>
{
public:
    Module() : Py::ExtensionModule<Module>("EquipGui")
    {
        initialize("This module is the EquipGui module.");// register with Python
    }

    ~Module() override {}

private:
};

PyObject *initModule() {
    return Base::Interpreter().addModule(new Module);
}

}// namespace EquipGui

/* Python entry */
PyMOD_INIT_FUNC(EquipGui)
{
    if (!Gui::Application::Instance) {
        PyErr_SetString(PyExc_ImportError, "Cannot load Gui module in console application.");
        PyMOD_Return(nullptr);
    }

    Base::Interpreter().runString("import Equip");
    Base::Interpreter().runString("import PartGui");

    // instantiating the commands
    CreateEquipCommands();

    EquipGui::Workbench::init();

    PyObject *mod = EquipGui::initModule();
    Base::Console().log("Loading GUI of Equip module... done\n");
    PyMOD_Return(mod);
}
