/***************************************************************************
 *   Copyright (c) 2023 Ji Qian Zhou <Zhouji963@163.com>                   *
 *                                                                         *
 ***************************************************************************/

#include "PreCompiled.h"
#ifndef _PreComp_
# include <sstream>
# include <QApplication>
# include <QMessageBox>

# include <BRepAdaptor_Curve.hxx>
# include <GeomAPI_ProjectPointOnCurve.hxx>
# include <TopoDS_Edge.hxx>
# include <TopoDS_Shape.hxx>
#endif

#include <App/Document.h>
#include <Gui/Application.h>
#include <Gui/Command.h>
#include <Gui/Control.h>
#include <Gui/MainWindow.h>
#include <Gui/Selection/SelectionFilter.h>
#include <Gui/Selection/SelectionObject.h>
#include "Mod/Part/App/PartFeature.h"


//===========================================================================
// CmdEquipShow THIS IS THE Equip Show COMMAND
//===========================================================================
DEF_STD_CMD(CmdEquipShow)

CmdEquipShow::CmdEquipShow()
  :Command("Equip_Show")
{
    sAppModule    = "Equip";
    sGroup        = QT_TR_NOOP("Equip");
    sMenuText     = QT_TR_NOOP("Equip Show function");
    sToolTipText  = QT_TR_NOOP("Shows a message");
    sWhatsThis    = "Equip_Show";
    sStatusTip    = QT_TR_NOOP("Equip Show function");
    sPixmap       = "EquipShow";
    sAccel        = "CTRL+H";
}

void CmdEquipShow::activated(int iMsg)
{
    Q_UNUSED(iMsg);
    QMessageBox::warning(Gui::getMainWindow(), QObject::tr("Equip"),
        QObject::tr("This is the Equip."));
    return;
}

void CreateEquipCommands(void)
{
    Gui::CommandManager &rcCmdMgr = Gui::Application::Instance->commandManager();
    rcCmdMgr.addCommand(new CmdEquipShow());
}
