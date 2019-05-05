# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Sun May  5 11:24:48 2019
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
s.Line(point1=(0.0, 0.0), point2=(0.13, 0.0))
s.HorizontalConstraint(entity=g[2], addUndoState=False)
s.Line(point1=(0.13, 0.0), point2=(0.13, 0.0075))
s.VerticalConstraint(entity=g[3], addUndoState=False)
s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s.Line(point1=(0.13, 0.0075), point2=(0.0, 0.0075))
s.HorizontalConstraint(entity=g[4], addUndoState=False)
s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s.Line(point1=(0.0, 0.0075), point2=(0.0, 0.0))
s.VerticalConstraint(entity=g[5], addUndoState=False)
s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
p = mdb.models['Model-1'].Part(name='plate', dimensionality=THREE_D, 
    type=EULERIAN)
p = mdb.models['Model-1'].parts['plate']
p.BaseSolidExtrude(sketch=s, depth=0.0007)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['plate']
s1 = p.features['Solid extrude-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s1)
s2 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
s2.autoDimension(objectList=(g[2], g[5]))
#: 2 dimensions added
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.241232, 
    farPlane=0.278933, width=0.200972, height=0.0864173, cameraPosition=(
    0.0889673, -0.00374496, 0.260432), cameraTarget=(0.0889673, -0.00374496, 
    0))
session.viewports['Viewport: 1'].view.fitView()
s2.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Line(point1=(0.0, 0.0), point2=(0.015, 0.0))
s.HorizontalConstraint(entity=g[2], addUndoState=False)
s.Line(point1=(0.015, 0.0), point2=(0.015, 0.002))
s.VerticalConstraint(entity=g[3], addUndoState=False)
s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s.Line(point1=(0.015, 0.002), point2=(0.02, 0.004))
s.undo()
s.undo()
s.undo()
s.Line(point1=(0.0, 0.0), point2=(0.015, 0.0))
s.HorizontalConstraint(entity=g[2], addUndoState=False)
s.Line(point1=(0.015, 0.0), point2=(0.03, 0.005))
s.undo()
s.undo()
s.undo()
#* Nothing to undo.
s.Line(point1=(0.0, 0.0), point2=(0.015, 0.0))
s.HorizontalConstraint(entity=g[2], addUndoState=False)
s.Line(point1=(0.015, 0.0), point2=(0.02, 0.015))
s.Line(point1=(0.02, 0.015), point2=(0.02, 0.02))
s.VerticalConstraint(entity=g[4], addUndoState=False)
s.Line(point1=(0.02, 0.02), point2=(0.0, 0.02))
s.HorizontalConstraint(entity=g[5], addUndoState=False)
s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s.Line(point1=(0.0, 0.02), point2=(0.0, 0.0))
s.VerticalConstraint(entity=g[6], addUndoState=False)
s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.931816, 
    farPlane=0.953802, width=0.114692, height=0.0493173, cameraPosition=(
    0.0146978, 0.00459575, 0.942809), cameraTarget=(0.0146978, 0.00459575, 0))
s.FilletByRadius(radius=0.0005, curve1=g[2], nearPoint1=(0.013687752187252, 
    -0.000126116909086704), curve2=g[3], nearPoint2=(0.0154833197593689, 
    0.00107308570295572))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.93838, 
    farPlane=0.947238, width=0.0462069, height=0.0198689, cameraPosition=(
    0.0151967, 0.00171653, 0.942809), cameraTarget=(0.0151967, 0.00171653, 0))
p = mdb.models['Model-1'].Part(name='press', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['press']
p.BaseShellExtrude(sketch=s, depth=0.0007)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['press']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(width=0.0484391, 
    height=0.0208287, viewOffsetX=-0.000102692, viewOffsetY=6.14098e-05)
mdb.saveAs(
    pathName='/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model')
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae".
p1 = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238252, 
    farPlane=0.329135, width=0.057742, height=0.0248939, 
    viewOffsetX=-0.0204341, viewOffsetY=0.0113308)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238358, 
    farPlane=0.329029, width=0.0577677, height=0.024905, cameraPosition=(
    0.233241, 0.158834, 0.168397), cameraUpVector=(-0.340473, 0.535787, 
    -0.772665), cameraTarget=(0.0694502, -0.00495634, 0.00460608), 
    viewOffsetX=-0.0204432, viewOffsetY=0.0113358)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238358, 
    farPlane=0.329029, width=0.0577679, height=0.024905, 
    viewOffsetX=-0.0210099, viewOffsetY=0.0119414)
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#400 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.666666)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.236767, 
    farPlane=0.33062, width=0.0761401, height=0.0328257, 
    viewOffsetX=-0.0195473, viewOffsetY=0.0139172)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.236632, 
    farPlane=0.330755, width=0.0760967, height=0.032807, viewOffsetX=0.0111215, 
    viewOffsetY=0.00648033)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.236632, 
    farPlane=0.330755, width=0.0760967, height=0.032807, viewOffsetX=0.0245094, 
    viewOffsetY=0.00478514)
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#10 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.666666)
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#10 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.234907, 
    farPlane=0.33248, width=0.0962667, height=0.0415027, viewOffsetX=0.0325817, 
    viewOffsetY=0.00342294)
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#20 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.333333)
p = mdb.models['Model-1'].parts['plate']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[4], sketchUpEdge=e[5], 
    sketchPlaneSide=SIDE1, origin=(0.065, 0.00375, 0.0007))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=0.26, gridSpacing=0.006, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.sketchOptions.setValues(decimalPlaces=3)
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['plate']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.Line(point1=(-0.065, 0.001249995), point2=(0.065, 0.0012500025))
s1.Line(point1=(0.065, 0.0012500025), point2=(0.1, 0.0))
s1.Line(point1=(0.1, 0.0), point2=(0.1, 0.0075))
s1.VerticalConstraint(entity=g[12], addUndoState=False)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['plate']
f1, e1, d2 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[4], sketchUpEdge=e1[4], 
    sketchPlaneSide=SIDE1, origin=(0.065, 0.00375, 0.0007))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.26, 
    gridSpacing=0.006, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(decimalPlaces=3)
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['plate']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.Line(point1=(0.0, 0.005), point2=(0.013, 0.005))
s.HorizontalConstraint(entity=g[10], addUndoState=False)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['plate']
p.deleteFeatures(('Partition edge-1', 'Partition edge-2', 'Partition edge-3', 
    'Partition edge-4', ))
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#10 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.333333)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.234739, 
    farPlane=0.332648, width=0.0961979, height=0.041473, 
    viewOffsetX=-0.0170819, viewOffsetY=0.0136312)
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#800 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.66666)
p = mdb.models['Model-1'].parts['plate']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[4], sketchUpEdge=e[11], 
    sketchPlaneSide=SIDE1, origin=(0.065, 0.00375, 0.0007))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=0.26, gridSpacing=0.006, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.sketchOptions.setValues(decimalPlaces=3)
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['plate']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.Line(point1=(-0.065, -0.0012500025), point2=(0.065, -0.00124995))
p = mdb.models['Model-1'].parts['plate']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#10 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e1[11], faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=0.00412065, 
    viewOffsetY=0.0092822)
p = mdb.models['Model-1'].parts['plate']
f1, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchUpEdge=e[1], 
    sketchPlaneSide=SIDE1, origin=(0.065, 0.00625, 0.0007))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.26, 
    gridSpacing=0.006, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(decimalPlaces=3)
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['plate']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#4 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.77)
p = mdb.models['Model-1'].parts['plate']
f, e1, d2 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchUpEdge=e1[1], 
    sketchPlaneSide=SIDE1, origin=(0.065, 0.00625, 0.0007))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=0.26, gridSpacing=0.006, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.sketchOptions.setValues(decimalPlaces=3)
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['plate']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.Line(point1=(0.0351, 0.00125), point2=(0.0351, -0.00625000004656613))
s1.VerticalConstraint(entity=g[10], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[2], entity2=g[10], addUndoState=False)
s1.CoincidentConstraint(entity1=v[7], entity2=g[6], addUndoState=False)
p = mdb.models['Model-1'].parts['plate']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#21 ]', ), )
e, d1 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e[1], faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237432, 
    farPlane=0.329955, width=0.0662851, height=0.028577, 
    viewOffsetX=0.00990591, viewOffsetY=0.00867178)
p = mdb.models['Model-1'].parts['plate']
p.deleteFeatures(('Partition edge-1', 'Partition edge-2', 'Partition face-1', 
    'Partition edge-3', 'Partition face-2', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.235402, 
    farPlane=0.331985, width=0.0909102, height=0.0391934, 
    viewOffsetX=0.00232315, viewOffsetY=0.00975697)
p = mdb.models['Model-1'].parts['plate']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e1, v1, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlaneNormalToEdge(edge=e1[0], cells=pickedCells, 
    point=p.InterestingPoint(edge=e1[0], rule=MIDDLE))
p = mdb.models['Model-1'].parts['plate']
del p.features['Partition cell-1']
p = mdb.models['Model-1'].parts['plate']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e, v2, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v2[1], normal=e[0], cells=pickedCells)
#* Feature creation failed.
p = mdb.models['Model-1'].parts['plate']
f1, e1, d2 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[4], sketchUpEdge=e1[4], 
    sketchPlaneSide=SIDE1, origin=(0.065, 0.00375, 0.0007))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.26, 
    gridSpacing=0.006, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(decimalPlaces=3)
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['plate']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.Line(point1=(-0.065, 0.0015), point2=(0.065, 0.00375))
s.CoincidentConstraint(entity1=v[4], entity2=g[5], addUndoState=False)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['plate']
p.DatumCsysByThreePoints(name='Datum csys-1', coordSysType=CARTESIAN, origin=(
    0.0, 0.0, 0.0), line1=(1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
p = mdb.models['Model-1'].parts['plate']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[4], sketchUpEdge=e[4], 
    sketchPlaneSide=SIDE1, origin=(0.065, 0.00375, 0.0007))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=0.26, gridSpacing=0.006, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.sketchOptions.setValues(decimalPlaces=3)
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['plate']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.Line(point1=(0.0, 0.005), point2=(0.13, 0.005))
s1.HorizontalConstraint(entity=g[6], addUndoState=False)
s1.dragEntity(entity=v[4], points=((0.0, 0.005), (0.0, 0.0045), (-0.0465, 
    0.0015), (-0.0645, 0.0015), (-0.0645, 0.003), (-0.0645, 0.0015), (-0.0645, 
    0.003), (-0.0645, 0.0015)))
s1.Line(point1=(0.1, 0.0075), point2=(0.1, 0.0))
s1.VerticalConstraint(entity=g[7], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237133, 
    farPlane=0.284431, width=0.243078, height=0.104523, cameraPosition=(
    0.08212, 0.0131191, 0.261132), cameraTarget=(0.08212, 0.0131191, 0.0007))
s1.dragEntity(entity=v[6], points=((0.1, 0.0075), (0.1005, 0.0075), (0.0495, 
    -0.0015), (0.039, -0.0015), (0.0405, -0.0105), (0.0375, -0.021)))
s1.dragEntity(entity=v[7], points=((0.0375, 0.0), (0.0375, 0.0), (0.0465, 
    0.0045), (0.042, 0.006), (0.036, 0.0105), (0.0345, 0.012)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.241387, 
    farPlane=0.280177, width=0.198695, height=0.0854384, cameraPosition=(
    0.0892375, 0.0124343, 0.261132), cameraTarget=(0.0892375, 0.0124343, 
    0.0007))
s1.dragEntity(entity=g[7], points=((0.0345, 0.00855447273701429), (0.0345, 
    0.009), (0.0315, 0.009)))
session.viewports['Viewport: 1'].view.setValues(width=0.20275, height=0.087182, 
    cameraPosition=(0.0906831, 0.0130146, 0.261132), cameraTarget=(0.0906831, 
    0.0130146, 0.0007))
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.235068, 
    farPlane=0.332319, width=0.0945244, height=0.0407516, 
    viewOffsetX=0.00375909, viewOffsetY=0.00977603)
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.77)
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#8 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.77)
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#1 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.77)
p = mdb.models['Model-1'].parts['plate']
p.deleteFeatures(('Partition edge-2', 'Partition edge-3', ))
p = mdb.models['Model-1'].parts['plate']
p.regenerate()
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#8 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.23)
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#200 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.23)
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#40 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.33333)
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#200 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.66666)
p = mdb.models['Model-1'].parts['plate']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#8000 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.66666)
p = mdb.models['Model-1'].parts['plate']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
v1, e1, d2 = p.vertices, p.edges, p.datums
p.PartitionCellByPlaneThreePoints(point1=v1[1], point2=v1[4], point3=v1[10], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.239907, 
    farPlane=0.327481, width=0.0421544, height=0.0181737, 
    viewOffsetX=0.0329459, viewOffsetY=0.0044294)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23983, 
    farPlane=0.327557, width=0.0421409, height=0.0181679, 
    viewOffsetX=0.0164814, viewOffsetY=0.00732711)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23983, 
    farPlane=0.327557, width=0.0421409, height=0.0181679, 
    viewOffsetX=0.000799142, viewOffsetY=0.00881809)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23983, 
    farPlane=0.327557, width=0.0421409, height=0.0181679, 
    viewOffsetX=-0.0127334, viewOffsetY=0.0106404)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23983, 
    farPlane=0.327557, width=0.0421409, height=0.0181679, 
    viewOffsetX=-0.0258249, viewOffsetY=0.0128493)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23983, 
    farPlane=0.327557, width=0.0421409, height=0.0181679, 
    viewOffsetX=-0.0269549, viewOffsetY=0.0126008)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23983, 
    viewOffsetX=-0.0120995, viewOffsetY=0.0123523)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23983, 
    width=0.0421409, height=0.0181679, viewOffsetX=0.00289375, 
    viewOffsetY=0.0104472)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23983, 
    width=0.0421409, height=0.0181679, viewOffsetX=0.0175011, 
    viewOffsetY=0.008404)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23983, 
    width=0.0421409, height=0.0181679, viewOffsetX=0.0277538, 
    viewOffsetY=0.00641602)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23983, 
    width=0.0421409, height=0.0181679, viewOffsetX=0.0367387, 
    viewOffsetY=0.00580858)
p = mdb.models['Model-1'].parts['plate']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
v2, e, d1 = p.vertices, p.edges, p.datums
p.PartitionCellByPlaneThreePoints(point1=v2[14], point2=v2[5], point3=v2[12], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.240135, 
    farPlane=0.327253, width=0.0381405, height=0.0164432, 
    viewOffsetX=0.0351857, viewOffsetY=0.0057193)
mdb.save()
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.2395, 
    farPlane=0.327887, width=0.0465561, height=0.0200714, viewOffsetX=0.038243, 
    viewOffsetY=0.00495781)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
openMdb(
    pathName='/home/fe1/bme.Finite-Element-Analysis-I/assignment4/press.cae')
#: The model database "/home/fe1/bme.Finite-Element-Analysis-I/assignment4/press.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['press'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
openMdb(
    pathName='/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae')
#: The model database "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].Material(name='platematerial')
mdb.models['Model-1'].materials['platematerial'].Plastic(table=((220000000.0, 
    0.0), (230000000.0, 0.0845), (250000000.0, 0.0969), (260000000.0, 0.1104), 
    (260000000.0, 0.1252), (270000000.0, 0.1412), (280000000.0, 0.1587), (
    290000000.0, 0.1775), (300000000.0, 0.1979), (310000000.0, 0.2197), (
    320000000.0, 0.2432), (330000000.0, 0.2684), (340000000.0, 0.2953), (
    350000000.0, 0.324), (360000000.0, 0.3546), (370000000.0, 0.3871), (
    380000000.0, 0.4216), (390000000.0, 0.4581), (400000000.0, 0.4968), (
    410000000.0, 0.5376), (420000000.0, 0.5807), (430000000.0, 0.6261), (
    440000000.0, 0.6739), (450000000.0, 0.7242), (460000000.0, 0.7769), (
    470000000.0, 0.8323), (480000000.0, 0.8903), (490000000.0, 0.951), (
    500000000.0, 1.0145), (510000000.0, 1.0809), (520000000.0, 1.1502), (
    530000000.0, 1.2225), (540000000.0, 1.2978), (550000000.0, 1.3763), (
    560000000.0, 1.458), (570000000.0, 1.5429), (580000000.0, 1.6312), (
    590000000.0, 1.723), (600000000.0, 1.8182), (610000000.0, 1.9169), (
    620000000.0, 2.0193), (630000000.0, 2.1254), (640000000.0, 2.2352), (
    650000000.0, 2.3489), (660000000.0, 2.4665), (670000000.0, 2.5881), (
    680000000.0, 2.7138), (690000000.0, 2.8436), (700000000.0, 2.9776), (
    710000000.0, 3.1158), (720000000.0, 3.2585), (730000000.0, 3.4055), (
    740000000.0, 3.5571), (750000000.0, 3.7132), (760000000.0, 3.8739), (
    770000000.0, 4.0394), (780000000.0, 4.2097)))
mdb.models['Model-1'].materials['platematerial'].Density(table=((2700.0, ), ))
mdb.models['Model-1'].materials['platematerial'].Elastic(table=((70000000000.0, 
    0.3), ))
mdb.models['Model-1'].Material(name='pressmaterial')
mdb.models['Model-1'].materials['pressmaterial'].Density(table=((2700.0, ), ))
mdb.models['Model-1'].materials['pressmaterial'].Elastic(table=((70000000000.0, 
    0.3), ))
mdb.models['Model-1'].EulerianSection(name='platesection', data={
    'platematerial-1': 'platematerial'})
p = mdb.models['Model-1'].parts['plate']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#f ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['Model-1'].parts['plate']
p.SectionAssignment(region=region, sectionName='platesection', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p1 = mdb.models['Model-1'].parts['press']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].HomogeneousShellSection(name='presssection', 
    preIntegrate=OFF, material='pressmaterial', thicknessType=UNIFORM, 
    thickness=0.001, thicknessField='', idealization=NO_IDEALIZATION, 
    poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
    useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
p = mdb.models['Model-1'].parts['press']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#3f ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['press']
p.SectionAssignment(region=region, sectionName='presssection', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['plate']
a.Instance(name='plate-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['press']
a.Instance(name='press-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238267, 
    farPlane=0.3364, width=0.0580648, height=0.0249677, viewOffsetX=-0.0231127, 
    viewOffsetY=0.011328)
a = mdb.models['Model-1'].rootAssembly
a.translate(instanceList=('press-1', ), vector=(0.0, 0.005, 0.0))
#: The instance press-1 was translated by 0., 5.E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23475, 
    farPlane=0.33703, width=0.0672429, height=0.0289143, 
    viewOffsetX=-0.0213361, viewOffsetY=0.0117332)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['plate']
s = p.features['Solid extrude-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s2 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
s2.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-1', previous='Initial', 
    timePeriod=0.001)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
mdb.models['Model-1'].ContactProperty('IntProp-1')
#: The interaction property "IntProp-1" has been created.
mdb.models['Model-1'].ContactExp(name='Int-1', createStepName='Step-1')
mdb.models['Model-1'].interactions['Int-1'].includedPairs.setValuesInStep(
    stepName='Step-1', useAllstar=ON)
mdb.models['Model-1'].interactions['Int-1'].contactPropertyAssignments.appendInStep(
    stepName='Step-1', assignments=((GLOBAL, SELF, 'IntProp-1'), ))
#: The interaction "Int-1" has been created.
mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON, 
    constraintEnforcementMethod=DEFAULT)
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
    formulation=FRICTIONLESS)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.2382, 
    farPlane=0.333579, width=0.0286223, height=0.0123075, 
    viewOffsetX=-0.027425, viewOffsetY=0.0141607)
a = mdb.models['Model-1'].rootAssembly
v11 = a.instances['press-1'].vertices
a.ReferencePoint(point=v11[0])
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238143, 
    farPlane=0.333637, width=0.030416, height=0.0130788, viewOffsetX=-0.026745, 
    viewOffsetY=0.0137181)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238087, 
    farPlane=0.333693, width=0.0304089, height=0.0130758, 
    viewOffsetX=-0.027314, viewOffsetY=0.0175701)
p1 = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['plate']
p.seedPart(size=0.0007, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['plate']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['press']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.save()
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae".
mdb.save()
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae".
p1 = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    interactions=OFF, constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
mdb.save()
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae".
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['press']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238869, 
    farPlane=0.33291, width=0.0216407, height=0.00930543, 
    viewOffsetX=-0.028624, viewOffsetY=0.0176302)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['plate-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#20 ]', ), )
region1=a.Set(vertices=verts1, name='m_Set-1')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['press-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#24 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-1')
mdb.models['Model-1'].Coupling(name='Constraint-1', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237845, 
    farPlane=0.333935, width=0.0336491, height=0.014469, 
    viewOffsetX=-0.0231676, viewOffsetY=0.016464)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Model-1'].parts['press']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.233372, 
    farPlane=0.338408, width=0.0821964, height=0.0353442, 
    viewOffsetX=-0.0326603, viewOffsetY=0.0197969)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.233227, 
    farPlane=0.338553, width=0.0821454, height=0.0353223, 
    viewOffsetX=0.00685191, viewOffsetY=0.00351922)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.233227, 
    farPlane=0.338553, width=0.0821454, height=0.0353223, 
    viewOffsetX=0.0144609, viewOffsetY=-0.00286885)
a = mdb.models['Model-1'].rootAssembly
instList = (a.instances['plate-1'], )
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['plate-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
rgn1 = a.Set(cells=cells1, name='Set-2')
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['plate-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#e ]', ), )
rgn2 = a.Set(cells=cells1, name='Set-2')
fract1 = (1, )
fract2 = (0, )
mdb.models['Model-1'].MaterialAssignment(name='Predefined Field-1', 
    instanceList=instList, useFields=False, assignmentList=((rgn1, fract1), (
    rgn2, fract2), ))
mdb.models['Model-1'].SmoothStepAmplitude(name='Amp-1', timeSpan=STEP, data=((
    0.0, 0.0), (0.001, 1.0)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.233227, 
    width=0.0821454, height=0.0353223, viewOffsetX=-0.0189224, 
    viewOffsetY=0.0204288)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[6], )
region = a.Set(referencePoints=refPoints1, name='Set-3')
mdb.models['Model-1'].DisplacementBC(name='displacement', 
    createStepName='Initial', region=region, u1=UNSET, u2=SET, u3=UNSET, 
    ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, 
    fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.239682, 
    farPlane=0.332098, width=0.0131595, height=0.00565857, 
    viewOffsetX=-0.0350634, viewOffsetY=0.0191741)
mdb.save()
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae".
mdb.models['Model-1'].boundaryConditions['displacement'].setValues(
    localCsys=None)
mdb.save()
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae".
openMdb(
    pathName='/home/fe1/bme.Finite-Element-Analysis-I/assignment4/press.cae')
#: The model database "/home/fe1/bme.Finite-Element-Analysis-I/assignment4/press.cae" has been opened.
a = mdb.models['press'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['press'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='step1')
openMdb(
    pathName='/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae')
#: The model database "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae" has been opened.
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models['Model-1'].boundaryConditions['displacement'].setValuesInStep(
    stepName='Step-1', u2=-0.0025, amplitude='Amp-1')
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.233596, 
    farPlane=0.344935, width=0.111972, height=0.0481475, 
    viewOffsetX=-0.00812499, viewOffsetY=0.00364823)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237595, 
    farPlane=0.340936, width=0.0701889, height=0.030181, 
    viewOffsetX=-0.0193208, viewOffsetY=0.00835423)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.237722, 
    farPlane=0.340809, width=0.0702264, height=0.0301972, cameraPosition=(
    0.237622, 0.176374, 0.164877), cameraUpVector=(-0.569918, 0.577303, 
    -0.584735), cameraTarget=(0.0706142, 0.00936672, -0.00213084), 
    viewOffsetX=-0.0193311, viewOffsetY=0.0083587)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.239964, 
    farPlane=0.338567, width=0.0454518, height=0.0195442, 
    viewOffsetX=-0.0264266, viewOffsetY=0.0110257)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.240048, 
    farPlane=0.338483, width=0.0454678, height=0.019551, 
    viewOffsetX=-0.0268511, viewOffsetY=0.0169127)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.276077, 
    farPlane=0.355937, width=0.0522921, height=0.0224855, cameraPosition=(
    -0.0656212, 0.133387, 0.262387), cameraUpVector=(0.0703922, 0.68465, 
    -0.725465), cameraTarget=(0.0697245, 0.0183776, 0.0340698), 
    viewOffsetX=-0.0308812, viewOffsetY=0.0194511)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.268834, 
    farPlane=0.363179, width=0.124864, height=0.053691, viewOffsetX=-0.0138458, 
    viewOffsetY=0.0241485)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.250179, 
    farPlane=0.403453, width=0.116199, height=0.0499651, cameraPosition=(
    -0.255115, -0.0123551, 0.0708174), cameraUpVector=(0.309058, 0.950986, 
    0.0104262), cameraTarget=(0.0319695, -0.00388437, 0.0363897), 
    viewOffsetX=-0.0128849, viewOffsetY=0.0224727)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.254914, 
    farPlane=0.398718, width=0.0729074, height=0.03135, viewOffsetX=-0.0229579, 
    viewOffsetY=0.0158506)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['plate-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#10 ]', ), )
region = a.Set(faces=faces1, name='Set-4')
mdb.models['Model-1'].XsymmBC(name='symmetryX', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.256588, 
    farPlane=0.399573, width=0.0733861, height=0.0315558, cameraPosition=(
    -0.236553, -0.0867021, 0.0889778), cameraUpVector=(-0.0227464, 0.937623, 
    -0.346908), cameraTarget=(0.0334211, 0.00387534, 0.0381407), 
    viewOffsetX=-0.0231087, viewOffsetY=0.0159547)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['plate-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#10000 ]', ), )
region = a.Set(faces=faces1, name='Set-5')
mdb.models['Model-1'].YsymmBC(name='symmetryY', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.213434, 
    farPlane=0.331896, width=0.129297, height=0.0555972, cameraPosition=(
    -0.132247, -0.0148266, 0.186789), cameraUpVector=(0.231787, 0.967512, 
    -0.100977), cameraTarget=(0.0625869, 0.0136993, -0.00876134))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.196804, 
    farPlane=0.348, width=0.119223, height=0.0512655, cameraPosition=(
    -0.187128, 0.0932655, -0.0641857), cameraUpVector=(0.587206, 0.791954, 
    0.167325), cameraTarget=(0.0667825, 0.00677315, 0.00696497))
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['plate-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#40080 ]', ), )
region = a.Set(faces=faces1, name='Set-6')
mdb.models['Model-1'].DisplacementBC(name='planeFix', createStepName='Initial', 
    region=region, u1=UNSET, u2=UNSET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=1, 
    activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=1)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['Model-1'].rootAssembly
rgn1 = a.instances['plate-1'].sets['Set-1']
a = mdb.models['Model-1'].rootAssembly
rgn2 = a.sets['Set-2']
fract1 = (1, )
fract2 = (0, )
mdb.models['Model-1'].predefinedFields['Predefined Field-1'].setValues(
    assignmentList=((rgn1, fract1), (rgn2, fract2), ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Error in job Job-1: SPECIFIED SURFACE ASSEMBLY_S_SURF-1 DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-1: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-1: SPECIFIED SURFACE ASSEMBLY_S_SURF-1 DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-1: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: NODE SET ASSEMBLY_SET-3 HAS NOT BEEN DEFINED
#: Job Job-1: Analysis Input File Processor aborted due to errors.
#: Error in job Job-1: Analysis Input File Processor exited with an error.
#: Job Job-1 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.197463, 
    farPlane=0.347341, width=0.122063, height=0.0524869, 
    viewOffsetX=0.000588419, viewOffsetY=0.000247278)
mdb.save()
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
del mdb.models['Model-1'].constraints['Constraint-1']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Model-1'].parts['press']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0444366, 
    farPlane=0.0720387, width=0.0214272, height=0.00921365, 
    viewOffsetX=-2.34747e-05, viewOffsetY=-0.00314113)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0467607, 
    farPlane=0.0686694, width=0.0225479, height=0.00969553, cameraPosition=(
    0.0258526, 0.0445185, 0.0438043), cameraUpVector=(-0.567651, 0.512777, 
    -0.644075), cameraTarget=(0.0101198, 0.00972691, -0.000168997), 
    viewOffsetX=-2.47024e-05, viewOffsetY=-0.00330541)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0411815, 
    farPlane=0.0631047, width=0.0198576, height=0.00853872, cameraUpVector=(
    -0.535922, 0.37713, -0.755354), cameraTarget=(0.0342655, 0.00160184, 
    0.00329355), viewOffsetX=-2.17551e-05, viewOffsetY=-0.00291103)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.039733, 
    farPlane=0.0645532, width=0.0385701, height=0.016585, 
    viewOffsetX=0.00139084, viewOffsetY=-0.00431706)
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0476784, 
    farPlane=0.0737481, width=0.0420115, height=0.0180648, cameraUpVector=(
    0.0201883, 0.556912, -0.830326), cameraTarget=(0.0100898, 0.011222, 
    -0.000925951))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0537004, 
    farPlane=0.0650637, width=0.0473178, height=0.0203465, cameraPosition=(
    0.0149802, 0.00781187, 0.0594939), cameraUpVector=(-0.0326435, 0.993587, 
    -0.10826), cameraTarget=(0.0100898, 0.011222, -0.000925957))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0529108, 
    farPlane=0.0658534, width=0.0515776, height=0.0221782, 
    viewOffsetX=1.65653e-05, viewOffsetY=0.000284277)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0521672, 
    farPlane=0.067301, width=0.0508527, height=0.0218665, cameraPosition=(
    0.0130944, 0.0223815, 0.0587156), cameraUpVector=(-0.0285741, 0.936821, 
    -0.34864), cameraTarget=(0.0101324, 0.0109009, -0.000828722), 
    viewOffsetX=1.63325e-05, viewOffsetY=0.000280282)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0482373, 
    farPlane=0.0720341, width=0.0470218, height=0.0202192, cameraPosition=(
    0.0255275, 0.0364798, 0.0520718), cameraUpVector=(-0.0147605, 0.811604, 
    -0.584022), cameraTarget=(0.00991318, 0.0107011, -0.000632598), 
    viewOffsetX=1.51021e-05, viewOffsetY=0.000259168)
p = mdb.models['Model-1'].parts['press']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#11 ]', ), )
s = p.faces
side12Faces = s.getSequenceFromMask(mask=('[#3f ]', ), )
p.Surface(side1Edges=side1Edges, side12Faces=side12Faces, name='pressSurface')
#: The surface 'pressSurface' has been created (6 faces, 2 edges).
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['m_Set-1']
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['press-1'].surfaces['pressSurface']
mdb.models['Model-1'].Coupling(name='Constraint-1', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Error in job Job-1: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-1: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-1: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-1: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: NODE SET ASSEMBLY_SET-3 HAS NOT BEEN DEFINED
#: Job Job-1: Analysis Input File Processor aborted due to errors.
#: Error in job Job-1: Analysis Input File Processor exited with an error.
#: Job Job-1 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['Set-3']
a = mdb.models['Model-1'].rootAssembly
region2=a.instances['press-1'].surfaces['pressSurface']
mdb.models['Model-1'].constraints['Constraint-1'].setValues(
    controlPoint=region1, surface=region2)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Error in job Job-1: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-1: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-1: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-1: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: NODE SET ASSEMBLY_SET-3 HAS NOT BEEN DEFINED
#: Job Job-1: Analysis Input File Processor aborted due to errors.
#: Error in job Job-1: Analysis Input File Processor exited with an error.
#: Job Job-1 aborted due to errors.
del mdb.models['Model-1'].rootAssembly.surfaces['s_Surf-1']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.198339, 
    farPlane=0.351283, width=0.122605, height=0.0527199, cameraPosition=(
    -0.204273, 0.0450391, 0.0450984), cameraUpVector=(0.294205, 0.64604, 
    -0.704327), cameraTarget=(0.0660911, 0.00917892, -0.00619857), 
    viewOffsetX=0.000591031, viewOffsetY=0.000248376)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Error in job Job-1: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-1: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-1: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-1: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-1: NODE SET ASSEMBLY_SET-3 HAS NOT BEEN DEFINED
#: Job Job-1: Analysis Input File Processor aborted due to errors.
#: Error in job Job-1: Analysis Input File Processor exited with an error.
#: Job Job-1 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(width=0.125076, 
    height=0.0537824, viewOffsetX=0.000880525, viewOffsetY=0.000452654)
o3 = session.openOdb(name='/home/fe1/bme.Finite-Element-Analysis-I/Job-1.odb')
#: Model: /home/fe1/bme.Finite-Element-Analysis-I/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       6
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#* There is no valid step data available on the database.If the analysis is 
#* running, the database must be closed and reopened once the results have been 
#* initialized. The requested operation has been cancelled.
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='Job-2', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=1, 
    activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=1)
del mdb.jobs['Job-1']
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Error in job Job-2: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-2: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-2: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-2: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-2: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-2: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-2: NODE SET ASSEMBLY_SET-3 HAS NOT BEEN DEFINED
#: Job Job-2: Analysis Input File Processor aborted due to errors.
#: Error in job Job-2: Analysis Input File Processor exited with an error.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].view.fitView()
mdb.jobs['Job-2'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Error in job Job-2: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-2: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-2: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-2: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-2: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-2: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-2: NODE SET ASSEMBLY_SET-3 HAS NOT BEEN DEFINED
#: Job Job-2: Analysis Input File Processor aborted due to errors.
#: Error in job Job-2: Analysis Input File Processor exited with an error.
#: Job Job-2 aborted due to errors.
mdb.save()
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.save()
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
a = mdb.models['Model-1'].rootAssembly
rgn1 = a.instances['plate-1'].sets['Set-1']
a = mdb.models['Model-1'].rootAssembly
rgn2 = a.sets['Set-2']
fract1 = (1, )
fract2 = (0, )
mdb.models['Model-1'].predefinedFields['Predefined Field-1'].setValues(
    assignmentList=((rgn1, fract1), (rgn2, fract2), ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.2013, 
    farPlane=0.339746, width=0.0444826, height=0.0191274, cameraPosition=(
    -0.199333, 0.0463851, 0.0469939), cameraUpVector=(0.32482, 0.729824, 
    -0.601539), cameraTarget=(0.0642202, 0.0114283, -0.00301077))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.214764, 
    farPlane=0.320801, width=0.0474579, height=0.0204068, cameraPosition=(
    -0.139006, 0.0255386, 0.17357), cameraUpVector=(0.0232157, 0.847516, 
    -0.530261), cameraTarget=(0.0608009, 0.012645, -0.00834761))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23473, 
    farPlane=0.340721, width=0.043374, height=0.0186507, 
    viewOffsetX=-0.0201574, viewOffsetY=0.00214359)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Error in job Job-2: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-2: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-2: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-2: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-2: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-2: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-2: NODE SET ASSEMBLY_SET-3 HAS NOT BEEN DEFINED
#: Job Job-2: Analysis Input File Processor aborted due to errors.
#: Error in job Job-2: Analysis Input File Processor exited with an error.
#: Job Job-2 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
del mdb.models['Model-1'].interactions['Int-1']
mdb.models['Model-1'].ContactExp(name='Int-1', createStepName='Step-1')
mdb.models['Model-1'].interactions['Int-1'].includedPairs.setValuesInStep(
    stepName='Step-1', useAllstar=ON)
mdb.models['Model-1'].interactions['Int-1'].contactPropertyAssignments.appendInStep(
    stepName='Step-1', assignments=((GLOBAL, SELF, 'IntProp-1'), ))
#: The interaction "Int-1" has been created.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238813, 
    farPlane=0.336638, width=0.000760929, height=0.000327197, 
    viewOffsetX=-0.0364899, viewOffsetY=0.0042178)
p = mdb.models['Model-1'].parts['press']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['plate']
s1 = p.features['Solid extrude-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s1)
s2 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
s2.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
p1 = mdb.models['Model-1'].parts['press']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.238821, 
    farPlane=0.33663, width=0.000676029, height=0.000290691, 
    viewOffsetX=-0.0365002, viewOffsetY=0.00421556)
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23153, 
    farPlane=0.343922, width=0.0767977, height=0.0330228, 
    viewOffsetX=-0.00925829, viewOffsetY=0.00248071)
a = mdb.models['Model-1'].rootAssembly
del a.features['RP-1']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.23362, 
    farPlane=0.341832, width=0.0549661, height=0.0236353, 
    viewOffsetX=-0.0168355, viewOffsetY=0.00371616)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('press-1', ), vector=(0.0, 0.0075, 0.0))
#: The instance press-1 was translated by 0., 7.5E-03, 0. with respect to the assembly coordinate system
a = mdb.models['Model-1'].rootAssembly
v31 = a.instances['press-1'].vertices
a.ReferencePoint(point=v31[0])
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('press-1', ), vector=(0.0, -0.0075, 0.0))
#: The instance press-1 was translated by 0., -7.5E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
p1 = mdb.models['Model-1'].parts['press']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['Model-1'].parts['press']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['m_Set-1']
mdb.models['Model-1'].constraints['Constraint-1'].setValues(
    controlPoint=region1)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.Job(name='Job-3', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=1, 
    activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=1)
mdb.jobs['Job-3'].submit(consistencyChecking=OFF)
#: The job input file "Job-3.inp" has been submitted for analysis.
#: Error in job Job-3: in keyword *BOUNDARY, file "Job-3.inp", line 6994: Unknown assembly node set SET-3
#: Error in job Job-3: in keyword *BOUNDARY, file "Job-3.inp", line 7024: Unknown assembly node set SET-3
#: Error in job Job-3: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-3: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-3: SPECIFIED SURFACE ASSEMBLY_PRESS-1_PRESSSURFACE DOES NOT EXIST. THIS SURFACE MUST BE DEFINED.
#: Error in job Job-3: AN ERROR HAS OCCURRED WHILE PROCESSING THE COUPLING OPTION. PLEASE CHECK THE DATA FILE FOR THE APPROPRIATE ERROR MESSAGES.
#: Error in job Job-3: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-3: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-3: NODE SET ASSEMBLY_SET-3 HAS NOT BEEN DEFINED
#: Job Job-3: Analysis Input File Processor aborted due to errors.
#: Error in job Job-3: Analysis Input File Processor exited with an error.
#: Job Job-3 aborted due to errors.
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Model-1'].parts['press']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['press']
p.seedPart(size=0.001, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['press']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Job-3'].submit(consistencyChecking=OFF)
#: The job input file "Job-3.inp" has been submitted for analysis.
#: Error in job Job-3: in keyword *BOUNDARY, file "Job-3.inp", line 7241: Unknown assembly node set SET-3
#: Error in job Job-3: in keyword *BOUNDARY, file "Job-3.inp", line 7271: Unknown assembly node set SET-3
#: Error in job Job-3: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-3: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-3: NODE SET ASSEMBLY_SET-3 HAS NOT BEEN DEFINED
#: Job Job-3: Analysis Input File Processor aborted due to errors.
#: Error in job Job-3: Analysis Input File Processor exited with an error.
#: Job Job-3 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
region = a.instances['press-1'].sets['Set-1']
mdb.models['Model-1'].boundaryConditions['displacement'].setValues(
    region=region)
del mdb.models['Model-1'].boundaryConditions['displacement']
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Model-1'].parts['press']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
p = mdb.models['Model-1'].parts['press']
n = p.nodes
nodes = n.getSequenceFromMask(mask=('[#1 ]', ), )
p.Set(nodes=nodes, name='Set-2')
#: The set 'Set-2' has been created (1 node).
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[15], )
region = a.Set(referencePoints=refPoints1, name='Set-7')
mdb.models['Model-1'].DisplacementBC(name='displacement', 
    createStepName='Initial', region=region, u1=UNSET, u2=SET, u3=UNSET, 
    ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, 
    fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
mdb.models['Model-1'].boundaryConditions['displacement'].setValuesInStep(
    stepName='Step-1', u2=-0.0025, amplitude='Amp-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Job-4', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=1, 
    activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=1)
mdb.jobs['Job-4'].submit(consistencyChecking=OFF)
#: The job input file "Job-4.inp" has been submitted for analysis.
#: Error in job Job-4: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-7 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-4: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-7 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-4: NODE SET ASSEMBLY_SET-7 HAS NOT BEEN DEFINED
#: Job Job-4: Analysis Input File Processor aborted due to errors.
#: Error in job Job-4: Analysis Input File Processor exited with an error.
#: Job Job-4 aborted due to errors.
mdb.save()
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae".
