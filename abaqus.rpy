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
