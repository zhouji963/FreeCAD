/***************************************************************************
 *   Copyright (c) 2023 Ji Qian Zhou <Zhouji963@163.com>                   *
 *                                                                         *
 ***************************************************************************/


#ifndef Equip_WORKBENCH_H
#define Equip_WORKBENCH_H

#include <Gui/Workbench.h>

namespace EquipGui {

class Workbench : public Gui::StdWorkbench
{
    TYPESYSTEM_HEADER_WITH_OVERRIDE();

public:
    Workbench();
    ~Workbench() override;

protected:
    Gui::MenuItem* setupMenuBar() const override;
    Gui::ToolBarItem* setupToolBars() const override;
};

} // namespace EquipGui


#endif // Equip_WORKBENCH_H 
