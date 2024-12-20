# trace generated using paraview version 5.12.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'CSV Reader'
cfdcsv = CSVReader(registrationName='cfd.csv', FileName=['/home/fderoma/OpenFOAM/fderoma-8/run/PRIN/paperMeasures_10L/lev2_P50M/P50M_349.06RPM_Re54.96/cfd.csv'])

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
cfdcsvDisplay = Show(cfdcsv, spreadSheetView1, 'SpreadSheetRepresentation')

# trace defaults for the display properties.
cfdcsvDisplay.Assembly = ''

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Table To Structured Grid'
tableToStructuredGrid1 = TableToStructuredGrid(registrationName='TableToStructuredGrid1', Input=cfdcsv)
tableToStructuredGrid1.XColumn = 'U'
tableToStructuredGrid1.YColumn = 'U'
tableToStructuredGrid1.ZColumn = 'U'

# destroy spreadSheetView1
Delete(spreadSheetView1)
del spreadSheetView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# Properties modified on tableToStructuredGrid1
tableToStructuredGrid1.WholeExtent = [0, 112, 0, 0, 0, 47]
tableToStructuredGrid1.XColumn = 'x_m'
tableToStructuredGrid1.YColumn = 'y_m'
tableToStructuredGrid1.ZColumn = 'z_m'

# show data in view
tableToStructuredGrid1Display = Show(tableToStructuredGrid1, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
tableToStructuredGrid1Display.Representation = 'Surface'
tableToStructuredGrid1Display.ColorArrayName = [None, '']
tableToStructuredGrid1Display.SelectTCoordArray = 'None'
tableToStructuredGrid1Display.SelectNormalArray = 'None'
tableToStructuredGrid1Display.SelectTangentArray = 'None'
tableToStructuredGrid1Display.OSPRayScaleArray = 'U'
tableToStructuredGrid1Display.OSPRayScaleFunction = 'Piecewise Function'
tableToStructuredGrid1Display.Assembly = ''
tableToStructuredGrid1Display.SelectOrientationVectors = 'None'
tableToStructuredGrid1Display.ScaleFactor = 0.017523708
tableToStructuredGrid1Display.SelectScaleArray = 'None'
tableToStructuredGrid1Display.GlyphType = 'Arrow'
tableToStructuredGrid1Display.GlyphTableIndexArray = 'None'
tableToStructuredGrid1Display.GaussianRadius = 0.0008761854
tableToStructuredGrid1Display.SetScaleArray = ['POINTS', 'U']
tableToStructuredGrid1Display.ScaleTransferFunction = 'Piecewise Function'
tableToStructuredGrid1Display.OpacityArray = ['POINTS', 'U']
tableToStructuredGrid1Display.OpacityTransferFunction = 'Piecewise Function'
tableToStructuredGrid1Display.DataAxesGrid = 'Grid Axes Representation'
tableToStructuredGrid1Display.PolarAxes = 'Polar Axes Representation'
tableToStructuredGrid1Display.ScalarOpacityUnitDistance = 0.010919657660838977
tableToStructuredGrid1Display.SelectInputVectors = [None, '']
tableToStructuredGrid1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
tableToStructuredGrid1Display.OSPRayScaleFunction.Points = [0.0176939747, 0.0, 0.5, 0.0, 0.1907321162, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
tableToStructuredGrid1Display.ScaleTransferFunction.Points = [-0.0810266346, 0.0, 0.5, 0.0, 0.5106526781, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
tableToStructuredGrid1Display.OpacityTransferFunction.Points = [-0.0810266346, 0.0, 0.5, 0.0, 0.5106526781, 1.0, 0.5, 0.0]

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
tableToStructuredGrid1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
tableToStructuredGrid1Display.DataAxesGrid.XTitleBold = 1
tableToStructuredGrid1Display.DataAxesGrid.XTitleFontSize = 26
tableToStructuredGrid1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
tableToStructuredGrid1Display.DataAxesGrid.YTitleBold = 1
tableToStructuredGrid1Display.DataAxesGrid.YTitleFontSize = 26
tableToStructuredGrid1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
tableToStructuredGrid1Display.DataAxesGrid.ZTitleBold = 1
tableToStructuredGrid1Display.DataAxesGrid.ZTitleFontSize = 26
tableToStructuredGrid1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
tableToStructuredGrid1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
tableToStructuredGrid1Display.DataAxesGrid.XLabelFontSize = 20
tableToStructuredGrid1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
tableToStructuredGrid1Display.DataAxesGrid.YLabelFontSize = 20
tableToStructuredGrid1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
tableToStructuredGrid1Display.DataAxesGrid.ZLabelFontSize = 20

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.07577500000000001, 0.587044218, 0.11277582]
renderView1.CameraFocalPoint = [0.07577500000000001, 0.0, 0.11277582]
renderView1.CameraViewUp = [1.0, 0.0, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

renderView1.ResetActiveCameraToPositiveY()

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# set scalar coloring
ColorBy(tableToStructuredGrid1Display, ('POINTS', 'U'))

# rescale color and/or opacity maps used to include current data range
tableToStructuredGrid1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tableToStructuredGrid1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# get 2D transfer function for 'U'
uTF2D = GetTransferFunction2D('U')

# rescale color and/or opacity maps used to exactly fit the current data range
tableToStructuredGrid1Display.RescaleTransferFunctionToDataRange(False, True)

# Properties modified on tableToStructuredGrid1Display
tableToStructuredGrid1Display.Position = [0.1, 0.0, 0.0]

# Properties modified on tableToStructuredGrid1Display.DataAxesGrid
tableToStructuredGrid1Display.DataAxesGrid.Position = [0.1, 0.0, 0.0]

# Properties modified on tableToStructuredGrid1Display.PolarAxes
tableToStructuredGrid1Display.PolarAxes.Translation = [0.1, 0.0, 0.0]

# create a new 'CSV Reader'
newPluronic_50M_350rpm_3Dcsv = CSVReader(registrationName='newPluronic_50M_350rpm_3D.csv', FileName=['/home/fderoma/OpenFOAM/fderoma-8/run/PRIN/paperMeasures_10L/lev2_P50M/P50M_349.06RPM_Re54.96/newPluronic_50M_350rpm_3D.csv'])

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
newPluronic_50M_350rpm_3DcsvDisplay = Show(newPluronic_50M_350rpm_3Dcsv, spreadSheetView1, 'SpreadSheetRepresentation')

# trace defaults for the display properties.
newPluronic_50M_350rpm_3DcsvDisplay.Assembly = ''

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Table To Structured Grid'
tableToStructuredGrid2 = TableToStructuredGrid(registrationName='TableToStructuredGrid2', Input=newPluronic_50M_350rpm_3Dcsv)
tableToStructuredGrid2.XColumn = 'U'
tableToStructuredGrid2.YColumn = 'U'
tableToStructuredGrid2.ZColumn = 'U'

# destroy spreadSheetView1
Delete(spreadSheetView1)
del spreadSheetView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# Properties modified on tableToStructuredGrid2
tableToStructuredGrid2.WholeExtent = [0, 112, 0, 0, 0, 47]
tableToStructuredGrid2.XColumn = 'x_m'
tableToStructuredGrid2.YColumn = 'y_m'
tableToStructuredGrid2.ZColumn = 'z_m'

# show data in view
tableToStructuredGrid2Display = Show(tableToStructuredGrid2, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
tableToStructuredGrid2Display.Representation = 'Surface'
tableToStructuredGrid2Display.ColorArrayName = [None, '']
tableToStructuredGrid2Display.SelectTCoordArray = 'None'
tableToStructuredGrid2Display.SelectNormalArray = 'None'
tableToStructuredGrid2Display.SelectTangentArray = 'None'
tableToStructuredGrid2Display.OSPRayScaleArray = 'U'
tableToStructuredGrid2Display.OSPRayScaleFunction = 'Piecewise Function'
tableToStructuredGrid2Display.Assembly = ''
tableToStructuredGrid2Display.SelectOrientationVectors = 'None'
tableToStructuredGrid2Display.ScaleFactor = 0.017523707649999998
tableToStructuredGrid2Display.SelectScaleArray = 'None'
tableToStructuredGrid2Display.GlyphType = 'Arrow'
tableToStructuredGrid2Display.GlyphTableIndexArray = 'None'
tableToStructuredGrid2Display.GaussianRadius = 0.0008761853824999999
tableToStructuredGrid2Display.SetScaleArray = ['POINTS', 'U']
tableToStructuredGrid2Display.ScaleTransferFunction = 'Piecewise Function'
tableToStructuredGrid2Display.OpacityArray = ['POINTS', 'U']
tableToStructuredGrid2Display.OpacityTransferFunction = 'Piecewise Function'
tableToStructuredGrid2Display.DataAxesGrid = 'Grid Axes Representation'
tableToStructuredGrid2Display.PolarAxes = 'Polar Axes Representation'
tableToStructuredGrid2Display.ScalarOpacityUnitDistance = 0.010919577813994018
tableToStructuredGrid2Display.SelectInputVectors = [None, '']
tableToStructuredGrid2Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
tableToStructuredGrid2Display.OSPRayScaleFunction.Points = [0.0176939747, 0.0, 0.5, 0.0, 0.1907321162, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
tableToStructuredGrid2Display.ScaleTransferFunction.Points = [-0.080088261, 0.0, 0.5, 0.0, 0.602344833, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
tableToStructuredGrid2Display.OpacityTransferFunction.Points = [-0.080088261, 0.0, 0.5, 0.0, 0.602344833, 1.0, 0.5, 0.0]

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
tableToStructuredGrid2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
tableToStructuredGrid2Display.DataAxesGrid.XTitleBold = 1
tableToStructuredGrid2Display.DataAxesGrid.XTitleFontSize = 26
tableToStructuredGrid2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
tableToStructuredGrid2Display.DataAxesGrid.YTitleBold = 1
tableToStructuredGrid2Display.DataAxesGrid.YTitleFontSize = 26
tableToStructuredGrid2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
tableToStructuredGrid2Display.DataAxesGrid.ZTitleBold = 1
tableToStructuredGrid2Display.DataAxesGrid.ZTitleFontSize = 26
tableToStructuredGrid2Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
tableToStructuredGrid2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
tableToStructuredGrid2Display.DataAxesGrid.XLabelFontSize = 20
tableToStructuredGrid2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
tableToStructuredGrid2Display.DataAxesGrid.YLabelFontSize = 20
tableToStructuredGrid2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
tableToStructuredGrid2Display.DataAxesGrid.ZLabelFontSize = 20

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on tableToStructuredGrid2Display
tableToStructuredGrid2Display.Position = [0.02, 0.0, 0.0]

# Properties modified on tableToStructuredGrid2Display.DataAxesGrid
tableToStructuredGrid2Display.DataAxesGrid.Position = [0.02, 0.0, 0.0]

# Properties modified on tableToStructuredGrid2Display.PolarAxes
tableToStructuredGrid2Display.PolarAxes.Translation = [0.02, 0.0, 0.0]

# Properties modified on tableToStructuredGrid2Display
tableToStructuredGrid2Display.Position = [0.2, 0.0, 0.0]

# Properties modified on tableToStructuredGrid2Display.DataAxesGrid
tableToStructuredGrid2Display.DataAxesGrid.Position = [0.2, 0.0, 0.0]

# Properties modified on tableToStructuredGrid2Display.PolarAxes
tableToStructuredGrid2Display.PolarAxes.Translation = [0.2, 0.0, 0.0]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# set scalar coloring
ColorBy(tableToStructuredGrid2Display, ('POINTS', 'U'))

# rescale color and/or opacity maps used to include current data range
tableToStructuredGrid2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tableToStructuredGrid2Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Open FOAM Reader'
p50M_34906RPM_Re5496foam = OpenFOAMReader(registrationName='P50M_349.06RPM_Re54.96.foam', FileName='/home/fderoma/OpenFOAM/fderoma-8/run/PRIN/paperMeasures_10L/lev2_P50M/P50M_349.06RPM_Re54.96/P50M_349.06RPM_Re54.96.foam')
p50M_34906RPM_Re5496foam.MeshRegions = ['internalMesh']
p50M_34906RPM_Re5496foam.CellArrays = ['U', 'p', 'strainRate']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# show data in view
p50M_34906RPM_Re5496foamDisplay = Show(p50M_34906RPM_Re5496foam, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# trace defaults for the display properties.
p50M_34906RPM_Re5496foamDisplay.Representation = 'Surface'
p50M_34906RPM_Re5496foamDisplay.ColorArrayName = ['POINTS', 'p']
p50M_34906RPM_Re5496foamDisplay.LookupTable = pLUT
p50M_34906RPM_Re5496foamDisplay.SelectTCoordArray = 'None'
p50M_34906RPM_Re5496foamDisplay.SelectNormalArray = 'None'
p50M_34906RPM_Re5496foamDisplay.SelectTangentArray = 'None'
p50M_34906RPM_Re5496foamDisplay.OSPRayScaleArray = 'p'
p50M_34906RPM_Re5496foamDisplay.OSPRayScaleFunction = 'Piecewise Function'
p50M_34906RPM_Re5496foamDisplay.Assembly = 'Hierarchy'
p50M_34906RPM_Re5496foamDisplay.SelectOrientationVectors = 'U'
p50M_34906RPM_Re5496foamDisplay.ScaleFactor = 0.02620000056922436
p50M_34906RPM_Re5496foamDisplay.SelectScaleArray = 'p'
p50M_34906RPM_Re5496foamDisplay.GlyphType = 'Arrow'
p50M_34906RPM_Re5496foamDisplay.GlyphTableIndexArray = 'p'
p50M_34906RPM_Re5496foamDisplay.GaussianRadius = 0.001310000028461218
p50M_34906RPM_Re5496foamDisplay.SetScaleArray = ['POINTS', 'p']
p50M_34906RPM_Re5496foamDisplay.ScaleTransferFunction = 'Piecewise Function'
p50M_34906RPM_Re5496foamDisplay.OpacityArray = ['POINTS', 'p']
p50M_34906RPM_Re5496foamDisplay.OpacityTransferFunction = 'Piecewise Function'
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid = 'Grid Axes Representation'
p50M_34906RPM_Re5496foamDisplay.PolarAxes = 'Polar Axes Representation'
p50M_34906RPM_Re5496foamDisplay.ScalarOpacityFunction = pPWF
p50M_34906RPM_Re5496foamDisplay.ScalarOpacityUnitDistance = 0.002796982661013304
p50M_34906RPM_Re5496foamDisplay.OpacityArrayName = ['POINTS', 'p']
p50M_34906RPM_Re5496foamDisplay.SelectInputVectors = ['POINTS', 'U']
p50M_34906RPM_Re5496foamDisplay.WriteLog = ''

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
p50M_34906RPM_Re5496foamDisplay.OSPRayScaleFunction.Points = [0.0176939747, 0.0, 0.5, 0.0, 0.1907321162, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
p50M_34906RPM_Re5496foamDisplay.ScaleTransferFunction.Points = [-1.0075047016143799, 0.0, 0.5, 0.0, 0.5777918696403503, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
p50M_34906RPM_Re5496foamDisplay.OpacityTransferFunction.Points = [-1.0075047016143799, 0.0, 0.5, 0.0, 0.5777918696403503, 1.0, 0.5, 0.0]

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.XTitleBold = 1
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.XTitleFontSize = 26
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.YTitleBold = 1
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.YTitleFontSize = 26
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.ZTitleBold = 1
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.ZTitleFontSize = 26
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.XLabelFontSize = 20
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.YLabelFontSize = 20
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
p50M_34906RPM_Re5496foamDisplay.DataAxesGrid.ZLabelFontSize = 20

# show color bar/color legend
p50M_34906RPM_Re5496foamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=p50M_34906RPM_Re5496foam)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'p']
clip1.Value = -0.21485641598701477

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.0, 0.0, 0.0710000041872263]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.0, 0.0, 0.0710000041872263]

# Properties modified on clip1
clip1.Invert = 0

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, 0.0, 0.0]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'p']
clip1Display.LookupTable = pLUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'p'
clip1Display.OSPRayScaleFunction = 'Piecewise Function'
clip1Display.Assembly = 'Hierarchy'
clip1Display.SelectOrientationVectors = 'U'
clip1Display.ScaleFactor = 0.023000000417232516
clip1Display.SelectScaleArray = 'p'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'p'
clip1Display.GaussianRadius = 0.0011500000208616258
clip1Display.SetScaleArray = ['POINTS', 'p']
clip1Display.ScaleTransferFunction = 'Piecewise Function'
clip1Display.OpacityArray = ['POINTS', 'p']
clip1Display.OpacityTransferFunction = 'Piecewise Function'
clip1Display.DataAxesGrid = 'Grid Axes Representation'
clip1Display.PolarAxes = 'Polar Axes Representation'
clip1Display.ScalarOpacityFunction = pPWF
clip1Display.ScalarOpacityUnitDistance = 0.002728197252222119
clip1Display.OpacityArrayName = ['POINTS', 'p']
clip1Display.SelectInputVectors = ['POINTS', 'U']
clip1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
clip1Display.OSPRayScaleFunction.Points = [0.0176939747, 0.0, 0.5, 0.0, 0.1907321162, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [-1.0075047016143799, 0.0, 0.5, 0.0, 0.5777918696403503, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [-1.0075047016143799, 0.0, 0.5, 0.0, 0.5777918696403503, 1.0, 0.5, 0.0]

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.XTitleBold = 1
clip1Display.DataAxesGrid.XTitleFontSize = 26
clip1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.YTitleBold = 1
clip1Display.DataAxesGrid.YTitleFontSize = 26
clip1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.ZTitleBold = 1
clip1Display.DataAxesGrid.ZTitleFontSize = 26
clip1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.XLabelFontSize = 20
clip1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.YLabelFontSize = 20
clip1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.ZLabelFontSize = 20

# hide data in view
Hide(p50M_34906RPM_Re5496foam, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=clip1)
clip2.ClipType = 'Plane'
clip2.HyperTreeGridClipper = 'Plane'
clip2.Scalars = ['POINTS', 'p']
clip2.Value = -0.21485641598701477

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [0.0, 0.0, 0.10100000351667404]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [0.0, 0.0, 0.10100000351667404]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# Properties modified on clip2
clip2.Invert = 0

# show data in view
clip2Display = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = ['POINTS', 'p']
clip2Display.LookupTable = pLUT
clip2Display.SelectTCoordArray = 'None'
clip2Display.SelectNormalArray = 'None'
clip2Display.SelectTangentArray = 'None'
clip2Display.OSPRayScaleArray = 'p'
clip2Display.OSPRayScaleFunction = 'Piecewise Function'
clip2Display.Assembly = 'Hierarchy'
clip2Display.SelectOrientationVectors = 'U'
clip2Display.ScaleFactor = 0.023000000417232516
clip2Display.SelectScaleArray = 'p'
clip2Display.GlyphType = 'Arrow'
clip2Display.GlyphTableIndexArray = 'p'
clip2Display.GaussianRadius = 0.0011500000208616258
clip2Display.SetScaleArray = ['POINTS', 'p']
clip2Display.ScaleTransferFunction = 'Piecewise Function'
clip2Display.OpacityArray = ['POINTS', 'p']
clip2Display.OpacityTransferFunction = 'Piecewise Function'
clip2Display.DataAxesGrid = 'Grid Axes Representation'
clip2Display.PolarAxes = 'Polar Axes Representation'
clip2Display.ScalarOpacityFunction = pPWF
clip2Display.ScalarOpacityUnitDistance = 0.0029185402675437674
clip2Display.OpacityArrayName = ['POINTS', 'p']
clip2Display.SelectInputVectors = ['POINTS', 'U']
clip2Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
clip2Display.OSPRayScaleFunction.Points = [0.0176939747, 0.0, 0.5, 0.0, 0.1907321162, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
clip2Display.ScaleTransferFunction.Points = [-1.0075047016143799, 0.0, 0.5, 0.0, 0.5777918696403503, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
clip2Display.OpacityTransferFunction.Points = [-1.0075047016143799, 0.0, 0.5, 0.0, 0.5777918696403503, 1.0, 0.5, 0.0]

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
clip2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.XTitleBold = 1
clip2Display.DataAxesGrid.XTitleFontSize = 26
clip2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.YTitleBold = 1
clip2Display.DataAxesGrid.YTitleFontSize = 26
clip2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.ZTitleBold = 1
clip2Display.DataAxesGrid.ZTitleFontSize = 26
clip2Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.XLabelFontSize = 20
clip2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.YLabelFontSize = 20
clip2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.ZLabelFontSize = 20

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=clip2)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]
slice1.PointMergeMethod = 'Uniform Binning'

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.057500001043081284, 0.0, 0.10100000351667404]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.057500001043081284, 0.0, 0.10100000351667404]

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'p']
slice1Display.LookupTable = pLUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'p'
slice1Display.OSPRayScaleFunction = 'Piecewise Function'
slice1Display.Assembly = 'Hierarchy'
slice1Display.SelectOrientationVectors = 'U'
slice1Display.ScaleFactor = 0.02020000070333481
slice1Display.SelectScaleArray = 'p'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'p'
slice1Display.GaussianRadius = 0.0010100000351667404
slice1Display.SetScaleArray = ['POINTS', 'p']
slice1Display.ScaleTransferFunction = 'Piecewise Function'
slice1Display.OpacityArray = ['POINTS', 'p']
slice1Display.OpacityTransferFunction = 'Piecewise Function'
slice1Display.DataAxesGrid = 'Grid Axes Representation'
slice1Display.PolarAxes = 'Polar Axes Representation'
slice1Display.SelectInputVectors = ['POINTS', 'U']
slice1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
slice1Display.OSPRayScaleFunction.Points = [0.0176939747, 0.0, 0.5, 0.0, 0.1907321162, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-0.20814937353134155, 0.0, 0.5, 0.0, 0.17004171013832092, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-0.20814937353134155, 0.0, 0.5, 0.0, 0.17004171013832092, 1.0, 0.5, 0.0]

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
slice1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.XTitleBold = 1
slice1Display.DataAxesGrid.XTitleFontSize = 26
slice1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.YTitleBold = 1
slice1Display.DataAxesGrid.YTitleFontSize = 26
slice1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.ZTitleBold = 1
slice1Display.DataAxesGrid.ZTitleFontSize = 26
slice1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.XLabelFontSize = 20
slice1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.YLabelFontSize = 20
slice1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.ZLabelFontSize = 20

# hide data in view
Hide(clip2, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1.SliceType)

# set active source
SetActiveSource(clip1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=clip1.ClipType)

# create a new 'Clip'
clip3 = Clip(registrationName='Clip3', Input=clip1)
clip3.ClipType = 'Plane'
clip3.HyperTreeGridClipper = 'Plane'
clip3.Scalars = ['POINTS', 'p']
clip3.Value = -0.21485641598701477

# init the 'Plane' selected for 'ClipType'
clip3.ClipType.Origin = [0.0, 0.0, 0.10100000351667404]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip3.HyperTreeGridClipper.Origin = [0.0, 0.0, 0.10100000351667404]

# Properties modified on clip3
clip3.Invert = 0

# Properties modified on clip3.ClipType
clip3.ClipType.Normal = [0.0, 1.0, 0.0]

# show data in view
clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip3Display.Representation = 'Surface'
clip3Display.ColorArrayName = ['POINTS', 'p']
clip3Display.LookupTable = pLUT
clip3Display.SelectTCoordArray = 'None'
clip3Display.SelectNormalArray = 'None'
clip3Display.SelectTangentArray = 'None'
clip3Display.OSPRayScaleArray = 'p'
clip3Display.OSPRayScaleFunction = 'Piecewise Function'
clip3Display.Assembly = 'Hierarchy'
clip3Display.SelectOrientationVectors = 'U'
clip3Display.ScaleFactor = 0.023000000417232516
clip3Display.SelectScaleArray = 'p'
clip3Display.GlyphType = 'Arrow'
clip3Display.GlyphTableIndexArray = 'p'
clip3Display.GaussianRadius = 0.0011500000208616258
clip3Display.SetScaleArray = ['POINTS', 'p']
clip3Display.ScaleTransferFunction = 'Piecewise Function'
clip3Display.OpacityArray = ['POINTS', 'p']
clip3Display.OpacityTransferFunction = 'Piecewise Function'
clip3Display.DataAxesGrid = 'Grid Axes Representation'
clip3Display.PolarAxes = 'Polar Axes Representation'
clip3Display.ScalarOpacityFunction = pPWF
clip3Display.ScalarOpacityUnitDistance = 0.0029148553887376463
clip3Display.OpacityArrayName = ['POINTS', 'p']
clip3Display.SelectInputVectors = ['POINTS', 'U']
clip3Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
clip3Display.OSPRayScaleFunction.Points = [0.0176939747, 0.0, 0.5, 0.0, 0.1907321162, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
clip3Display.ScaleTransferFunction.Points = [-1.0075047016143799, 0.0, 0.5, 0.0, 0.5775427222251892, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
clip3Display.OpacityTransferFunction.Points = [-1.0075047016143799, 0.0, 0.5, 0.0, 0.5775427222251892, 1.0, 0.5, 0.0]

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
clip3Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.XTitleBold = 1
clip3Display.DataAxesGrid.XTitleFontSize = 26
clip3Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.YTitleBold = 1
clip3Display.DataAxesGrid.YTitleFontSize = 26
clip3Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.ZTitleBold = 1
clip3Display.DataAxesGrid.ZTitleFontSize = 26
clip3Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.XLabelFontSize = 20
clip3Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.YLabelFontSize = 20
clip3Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.ZLabelFontSize = 20

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
clip3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice2 = Slice(registrationName='Slice2', Input=clip3)
slice2.SliceType = 'Plane'
slice2.HyperTreeGridSlicer = 'Plane'
slice2.SliceOffsetValues = [0.0]
slice2.PointMergeMethod = 'Uniform Binning'

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [0.0, 0.057500001043081284, 0.10100000351667404]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice2.HyperTreeGridSlicer.Origin = [0.0, 0.057500001043081284, 0.10100000351667404]

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice2.SliceType)

# show data in view
slice2Display = Show(slice2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['POINTS', 'p']
slice2Display.LookupTable = pLUT
slice2Display.SelectTCoordArray = 'None'
slice2Display.SelectNormalArray = 'None'
slice2Display.SelectTangentArray = 'None'
slice2Display.OSPRayScaleArray = 'p'
slice2Display.OSPRayScaleFunction = 'Piecewise Function'
slice2Display.Assembly = 'Hierarchy'
slice2Display.SelectOrientationVectors = 'U'
slice2Display.ScaleFactor = 0.02020000070333481
slice2Display.SelectScaleArray = 'p'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'p'
slice2Display.GaussianRadius = 0.0010100000351667404
slice2Display.SetScaleArray = ['POINTS', 'p']
slice2Display.ScaleTransferFunction = 'Piecewise Function'
slice2Display.OpacityArray = ['POINTS', 'p']
slice2Display.OpacityTransferFunction = 'Piecewise Function'
slice2Display.DataAxesGrid = 'Grid Axes Representation'
slice2Display.PolarAxes = 'Polar Axes Representation'
slice2Display.SelectInputVectors = ['POINTS', 'U']
slice2Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
slice2Display.OSPRayScaleFunction.Points = [0.0176939747, 0.0, 0.5, 0.0, 0.1907321162, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [-0.6103413105010986, 0.0, 0.5, 0.0, 0.5775427222251892, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [-0.6103413105010986, 0.0, 0.5, 0.0, 0.5775427222251892, 1.0, 0.5, 0.0]

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
slice2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.XTitleBold = 1
slice2Display.DataAxesGrid.XTitleFontSize = 26
slice2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.YTitleBold = 1
slice2Display.DataAxesGrid.YTitleFontSize = 26
slice2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.ZTitleBold = 1
slice2Display.DataAxesGrid.ZTitleFontSize = 26
slice2Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.XLabelFontSize = 20
slice2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.YLabelFontSize = 20
slice2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.ZLabelFontSize = 20

# hide data in view
Hide(clip3, renderView1)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1234, 761)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.08721392154693604, -1.1228346810752745, 0.10100000351667404]
renderView1.CameraFocalPoint = [0.08721392154693604, 0.0, 0.10100000351667404]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.29061099996389594


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------
