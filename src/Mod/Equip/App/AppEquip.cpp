/***************************************************************************
 *   Copyright (c) 2023 Ji Qian Zhou <Zhouji963@163.com>                   *
 *                                                                         *
 ***************************************************************************/

#include "PreCompiled.h"

#include <Base/Console.h>
#include <Base/PyObjectBase.h>

#include <Base/Interpreter.h>
#include <Base/Parameter.h>


namespace Equip 
{
class Module : public Py::ExtensionModule<Module>
{
public:
    Module() : Py::ExtensionModule<Module>("Equip")
    {
        initialize("This module is the Equip module.");// register with Python
    }

    ~Module() override {}

private:
};

PyObject *initModule()
{
    return Base::Interpreter().addModule(new Module);
}

}// namespace Equip

/* Python entry */
PyMOD_INIT_FUNC(Equip)
{
    try {
        Base::Interpreter().runString("import Part");
    }
    catch (const Base::Exception &e) {
        PyErr_SetString(PyExc_ImportError, e.what());
        PyMOD_Return(nullptr);
    }

    PyObject *mod = Equip::initModule();
    Base::Console().log("Loading Equip module... done\n");

    // Add types to module

    PyMOD_Return(mod);
}
