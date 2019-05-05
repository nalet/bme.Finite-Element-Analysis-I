# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_24-22.31.09 126547
# Run by fe1 on Sun May  5 21:13:46 2019
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
openMdb(
    pathName='/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae')
#: The model database "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.Job(name='Job-5', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=1, 
    activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=1)
mdb.jobs['Job-5'].submit(consistencyChecking=OFF)
#: The job input file "Job-5.inp" has been submitted for analysis.
#: Error in job Job-5: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-7 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-5: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-7 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-5: NODE SET ASSEMBLY_SET-7 HAS NOT BEEN DEFINED
#: Job Job-5: Analysis Input File Processor aborted due to errors.
#: Error in job Job-5: Analysis Input File Processor exited with an error.
#: Job Job-5 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.229992, 
    farPlane=0.348538, width=0.155422, height=0.0668311, 
    viewOffsetX=0.00437775, viewOffsetY=0.00255648)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.235311, 
    farPlane=0.343219, width=0.0940418, height=0.0404377, 
    viewOffsetX=-0.0124417, viewOffsetY=0.00831935)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['m_Set-1']
mdb.models['Model-1'].boundaryConditions['displacement'].setValues(
    region=region)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-5'].submit(consistencyChecking=OFF)
#: The job input file "Job-5.inp" has been submitted for analysis.
#: Job Job-5: Analysis Input File Processor completed successfully.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
#: Error in job Job-5: MPC-TYPE CONSTRAINS CAN NOT BE IMPOSED ON EULERIAN NODES.
#: Job Job-5: Abaqus/Explicit Packager aborted due to errors.
#: Error in job Job-5: Abaqus/Explicit Packager exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job Job-5 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
mdb.save()
#: The model database has been saved to "/home/fe1/bme.Finite-Element-Analysis-I/assignment5/model.cae".
