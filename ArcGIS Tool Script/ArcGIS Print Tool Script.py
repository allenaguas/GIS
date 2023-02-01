import arcpy

#Set variables
arcpy.mp.ArcGISProject('CURRENT')
aprx = arcpy.mp.ArcGISProject('CURRENT')
TCG4232_USNG_GRIDS = "TCG4232_USNG_GRIDS"
Output_Folder = arcpy.GetParameterAsText(0)


#Execute Select
arcpy.env.overwriteOutput = True
TCG4232_USNG_GRIDS_Selection = "P:/PROJECTS/RP_Quality_Control_cGIS/MapSalesArcProProject/MapSalesLive1211/MapSalesLive/ExportedGrids.gdb/TCG4232_USNG_GRIDS_Selection"
arcpy.analysis.Select(in_features=TCG4232_USNG_GRIDS, out_feature_class=TCG4232_USNG_GRIDS_Selection, where_clause="")

#Add selected grid to map contents
arcpy.env.workspace = r"P:/PROJECTS/RP_Quality_Control_cGIS/MapSalesArcProProject/MapSalesLive1211/MapSalesLive/ExportedGrids.gdb"
aprx = arcpy.mp.ArcGISProject('CURRENT')
map = aprx.listMaps("Map")[0]
map.addDataFromPath(TCG4232_USNG_GRIDS_Selection)

#list of layer names that you want to be turned off.
p = arcpy.mp.ArcGISProject("Current")
m = p.listMaps("Map")[0]
layer_names = ['TCG4232_USNG_GRIDS_Selection','TCG4232_USNG_GRIDS']
lyrList = m.listLayers()
for lyr in lyrList:
    lyr.visible = True
    if lyr.name in layer_names:
        lyr.visible = False

#Print to PDF
try:
    aprx = arcpy.mp.ArcGISProject('CURRENT')
    l = aprx.listLayouts()[0]
    l.mapSeries.refresh()

    if l.mapSeries is not None:
        ms = l.mapSeries
        if ms.enabled:
            ms = l.mapSeries
            indexLyr = "TCG4232_USNG_GRIDS_Selection"
            ms.exportToPDF(Output_Folder,"ALL",
                "",
                "PDF_SINGLE_FILE",
                150,
                "FASTEST",
                True,
                "ADAPTIVE",
                True,
                "LAYERS_ONLY",
                True,
                80,
                True,
                False)
except Exception as e:
    print(f"Error: {e.args[0]}")

#Delete selected layer    
arcpy.management.Delete("TCG4232_USNG_GRIDS_Selection", '')
