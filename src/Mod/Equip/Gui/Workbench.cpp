/***************************************************************************
 *   Copyright (c) 2023 Ji Qian Zhou <Zhouji963@163.com>                   *
 *                                                                         *
 ***************************************************************************/

#include "PreCompiled.h"

#include <Gui/MenuManager.h>
#include <Gui/ToolBarManager.h>

#include "Workbench.h"


using namespace EquipGui;

/// @namespace EquipGui @class Workbench
TYPESYSTEM_SOURCE(EquipGui::Workbench, Gui::StdWorkbench)

Workbench::Workbench()
{
}

Workbench::~Workbench()
{
}

Gui::MenuItem *Workbench::setupMenuBar() const
{
    Gui::MenuItem *root = StdWorkbench::setupMenuBar();
    Gui::MenuItem *item = root->findItem("&Windows");

	Gui::MenuItem* Equip = new Gui::MenuItem;
	root->insertItem(item, Equip);
	Equip->setCommand("Equip");
	*Equip << "Equip_Show";
	*Equip << "Equip_CylinderShell";
	*Equip << "Equip_SphericalHead";

    return root;
}

Gui::ToolBarItem *Workbench::setupToolBars() const
{
    Gui::ToolBarItem *root = StdWorkbench::setupToolBars();

    Gui::ToolBarItem* Equip = new Gui::ToolBarItem(root);
    Equip->setCommand( "Equip" );
      *Equip << "Equip_Show";
	  *Equip << "Equip_CylinderShell";
	  *Equip << "Equip_SphericalHead";

    return root;
}
