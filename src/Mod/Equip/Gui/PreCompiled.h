/***************************************************************************
 *   Copyright (c) 2023 Ji Qian Zhou <Zhouji963@163.com>                   *
 *                                                                         *
 ***************************************************************************/

#ifndef GUI_PRECOMPILED_H
#define GUI_PRECOMPILED_H

#include <FCConfig.h>

#ifdef _PreComp_

// STL
#include <sstream>

// Qt
#include <QAction>
#include <QApplication>
#include <QMenu>
#include <QMessageBox>
#include <QTimer>

// OpenCasCade
#include <BRepAdaptor_Curve.hxx>
#include <GeomAbs_Shape.hxx>
#include <GeomAPI_ProjectPointOnCurve.hxx>
#include <TopExp.hxx>
#include <TopoDS_Edge.hxx>
#include <TopoDS_Shape.hxx>
#include <TopTools_IndexedDataMapOfShapeListOfShape.hxx>
#include <TopTools_IndexedMapOfShape.hxx>
#include <TopTools_ListIteratorOfListOfShape.hxx>

#endif  //_PreComp_

#endif // GUI_PRECOMPILED_H
