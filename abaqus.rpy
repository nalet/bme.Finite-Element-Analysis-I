# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Tue May  7 09:33:24 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=293.952056884766, 
    height=168.578323364258)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Line(point1=(0.0, 0.0), point2=(0.003, 0.0))
s.HorizontalConstraint(entity=g[2], addUndoState=False)
s.Line(point1=(0.003, 0.0), point2=(0.015, 0.003))
s.undo()
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.Line(point1=(0.0, 0.0), point2=(0.003, 0.0))
s1.HorizontalConstraint(entity=g[2], addUndoState=False)
s1.Line(point1=(0.003, 0.0), point2=(0.003, 0.015))
s1.VerticalConstraint(entity=g[3], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s1.Line(point1=(0.003, 0.015), point2=(0.0, 0.015))
s1.HorizontalConstraint(entity=g[4], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s1.Line(point1=(0.0, 0.015), point2=(0.0, 0.0))
s1.VerticalConstraint(entity=g[5], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
p = mdb.models['Model-1'].Part(name='sample', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['sample']
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['sample']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0271003, 
    farPlane=0.034088, width=0.033783, height=0.0145266, viewOffsetX=0.0002762, 
    viewOffsetY=0.000194083)
p = mdb.models['Model-1'].parts['sample']
v1, e, d1, n = p.vertices, p.edges, p.datums, p.nodes
p.ReferencePoint(point=p.InterestingPoint(edge=e[3], rule=MIDDLE))
p = mdb.models['Model-1'].parts['sample']
r = p.referencePoints
refPoints=(r[2], )
p.Set(referencePoints=refPoints, name='RP-Pull')
#: The set 'RP-Pull' has been created (1 reference point).
p = mdb.models['Model-1'].parts['sample']
p.DatumCsysByThreePoints(name='Fiber-CSYS', coordSysType=CARTESIAN, origin=(
    0.0, 0.0, 0.0), line1=(1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
p = mdb.models['Model-1'].parts['sample']
p.DatumAxisByPrincipalAxis(principalAxis=YAXIS)
p = mdb.models['Model-1'].parts['sample']
v2, d2 = p.vertices, p.datums
p.DatumAxisByRotation(line=d2[5], point=v2[1], angle=45.0)
p = mdb.models['Model-1'].parts['sample']
del p.features['Datum axis-2']
p = mdb.models['Model-1'].parts['sample']
v1, d1 = p.vertices, p.datums
p.DatumAxisByRotation(line=d1[5], point=v1[1], angle=-45.0)
p = mdb.models['Model-1'].parts['sample']
p.deleteFeatures(('Datum axis-1', 'Datum axis-2', ))
mdb.saveAs(
    pathName='/home/fe1/bme.Finite-Element-Analysis-I/assignment6/model')
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment6/model.cae".
p = mdb.models['Model-1'].parts['sample']
del p.features['Fiber-CSYS']
p = mdb.models['Model-1'].parts['sample']
e1 = p.edges
p.DatumCsysByTwoLines(CARTESIAN, line1=e1[1], line2=e1[0], name='Fiber-CSYS')
p = mdb.models['Model-1'].parts['sample']
del p.features['Fiber-CSYS']
p = mdb.models['Model-1'].parts['sample']
p.DatumAxisByPrincipalAxis(principalAxis=YAXIS)
p = mdb.models['Model-1'].parts['sample']
v2, d2 = p.vertices, p.datums
p.DatumAxisByRotation(line=d2[9], point=v2[1], angle=45.0)
p = mdb.models['Model-1'].parts['sample']
v1, d1 = p.vertices, p.datums
p.DatumAxisByRotation(line=d1[9], point=v1[1], angle=-45.0)
p = mdb.models['Model-1'].parts['sample']
d2 = p.datums
p.DatumCsysByTwoLines(CARTESIAN, line1=d2[10], line2=d2[11], name='Fiber-CSYS')
mdb.save()
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment6/model.cae".
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='sample_material')
mdb.models['Model-1'].materials['sample_material'].Hyperelastic(
    materialType=ANISOTROPIC, anisotropicType=HOLZAPFEL, localDirections=2, 
    table=((55000.0, 1e-08, 65000000.0, 85.0, 0.2), ))
p = mdb.models['Model-1'].parts['sample']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(faces=faces)
orientation = mdb.models['Model-1'].parts['sample'].datums[12]
mdb.models['Model-1'].parts['sample'].MaterialOrientation(region=region, 
    orientationType=SYSTEM, axis=AXIS_3, localCsys=orientation, fieldName='', 
    additionalRotationType=ROTATION_NONE, angle=0.0, 
    additionalRotationField='', stackDirection=STACK_3)
#: Specified material orientation has been assigned to the selected regions.
mdb.save()
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment6/model.cae".
