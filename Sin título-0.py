from __future__ import division
import gdal
from osgeo.gdalconst import *
import numpy as np
from osgeo import ogr



def vecindad(distancia, np_array,punto):
	np_x = np_array.shape[0]
	np_y = np_array.shape[1]
	radio = distancia
	#print punto
	suma = 0
	puntos=0
	for x in xrange(radio):
		for y in xrange(radio):
			if punto[0]-x>0 and punto[1]-y>0:
				#print "cuadrante III :"+str(np_array[punto[0]-x][punto[1]-y])
				#suma+=np_array[punto[0]-x][punto[1]-y]
				if np_array[punto[0]-x][punto[1]-y]< 40.5:
					suma+=1
			if punto[0]+x< np_x and punto[1]+y<np_y:
				#print "cuadrante I :"+str(np_array[punto[0]+x][punto[1]+y])
				#suma+=np_array[punto[0]+x][punto[1]+y]
				if np_array[punto[0]+x][punto[1]+y]< 40.5:
					suma+=1

			if punto[0]+x< np_x and punto[1]-y>0:
				#print "cuadrante II :"+str(np_array[punto[0]+x][punto[1]-y])
				#suma+=np_array[punto[0]+x][punto[1]-y]
				if np_array[punto[0]+x][punto[1]-y]< 40.5:
					suma+=1
				
			if punto[0]-x>0 and punto[1]+y<np_y:
				#print "cuadrante IV :"+str(np_array[punto[0]-x][punto[1]+y])
				#suma+=np_array[punto[0]-x][punto[1]+y]
				if np_array[punto[0]-x][punto[1]+y]< 40.5:
					suma+=1
	#print "porcentaje vecindad menor al punto"+str((suma/(radio*radio*4))*100)		
	return (suma/(radio*radio*4))*100



#uri de capa activa
gdal_ndvi = gdal.Open("/Users/meraioth/Desktop/NDVI.tif")
gdal_dem = gdal.Open("/Users/meraioth/Desktop/dem_alig.tif",GA_Update);

uri_lines ='/Users/meraioth/Desktop/dem_esri.shp'
uri_polygons = '/Users/meraioth/Desktop/builds.shp'
uri_polygons2 = '/Users/meraioth/Desktop/builds2.shp'
uri_final = '/Users/meraioth/Desktop/buildings_final.shp'

#ogr_ds = ogr.GetDriverByName("ESRI Shapefile").CreateDataSource(uri_lines)
#contour_shp = ogr_ds.CreateLayer('contour')
#
#
#np_ndvi = np.array(gdal_ndvi.GetRasterBand(1).ReadAsArray())
#np_dem = np.array(gdal_dem.GetRasterBand(1).ReadAsArray())
#
#count = 0
#total_terreno = 0
#driver = gdal_dem.GetDriver()
#
#field_defn = ogr.FieldDefn("ID", ogr.OFTInteger)
#contour_shp.CreateField(field_defn)
#field_defn = ogr.FieldDefn("elev", ogr.OFTReal)
#contour_shp.CreateField(field_defn)
#
##Generate Contourlines
#gdal.ContourGenerate(gdal_dem.GetRasterBand(1), 2, 0, [], 0, 0, contour_shp, 0, 1)
#ogr_ds = None

import processing
#processing.runalg("qgis:linestopolygons",uri_lines,uri_polygons)

processing.runalg('qgis:exportaddgeometrycolumns', uri_polygons, 1 , uri_polygons2)
expression = '"area" > 5.99467533225426e-08'
processing.runandload('qgis:selectbyexpression', uri_polygons2, expression, 1)
processing.runandload('qgis:saveselectedfeatures', uri_polygons2, uri_final)

# for x in xrange(np_dem.shape[0]):
# 	for y in xrange(np_dem.shape[1]):
#          if np_ndvi[x][y]>0.17:
#             if np_dem[x][y]<40.5 :
#                 np_dem[x][y]=35

#for x in xrange(np_dem.shape[0]):
#    for y in xrange(np_dem.shape[1]):
#        #print "punto"+str([x,y])
#        if np_dem[x][y]>40.5 :
#            if vecindad(5,np_dem,[x,y])>75:
#                np_dem[x][y]=35
#            
#

gdal_dem.GetRasterBand(1).WriteArray(np_dem)
print "paso"
gdal_dem= None



#from osgeo.gdalconst import *
#
#driver = gdal_dem.GetDriver()
#out_dem = driver.Create("/Users/meraioth/Desktop/outdem.tif", np_dem.shape[1], np_dem.shape[0], 1, GDT_Float32)
#
#outBand = out_dem.GetRasterBand(1)
#outData = np.copy(np_dem)
#
## write the data
#outBand.WriteArray(outData, 0, 0)
#
## flush data to disk, set the NoData value and calculate stats
#outBand.FlushCache()
#outBand.SetNoDataValue(-99)
#
## georeference the image and set the projection
#out_dem.SetGeoTransform(gdal_dem.GetGeoTransform())
#out_dem.SetProjection(gdal_dem.GetProjection())
#
#del outData
#