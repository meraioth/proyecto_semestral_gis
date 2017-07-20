from __future__ import division
import gdal
from osgeo.gdalconst import *
import numpy as np
from osgeo import ogr
import processing



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



#uri de capa ndvi y dem
gdal_ndvi = gdal.Open("/Users/meraioth/Desktop/NDVI.tif")
gdal_dem = gdal.Open("/Users/meraioth/Desktop/dem_alig.tif",GA_Update);
#uri de capa lineas,polygonos sin area, poligonos con area y filtrada
uri_lines ='/Users/meraioth/Desktop/dem_esri.shp'
uri_polygons = '/Users/meraioth/Desktop/builds.shp'
uri_polygons2 = '/Users/meraioth/Desktop/builds2.shp'
uri_final = '/Users/meraioth/Desktop/buildings_final.shp'
#raster to array
np_ndvi = np.array(gdal_ndvi.GetRasterBand(1).ReadAsArray())
np_dem = np.array(gdal_dem.GetRasterBand(1).ReadAsArray())

driver = gdal_dem.GetDriver()

#primero eliminamos los arboles de la capa dem cuando ndvi<0.17 (nasa con umbral) llevamos el dem a negro

for x in xrange(np_dem.shape[0]):
	for y in xrange(np_dem.shape[1]):
         if np_ndvi[x][y]>0.17:
         	np_dem[x][y]=35
#segundo llevamos a negro todo lo que sea inferior a 2-3 mts
for x in xrange(np_dem.shape[0]):
	for y in xrange(np_dem.shape[1]):
		 if np_dem[x][y]<40.9 :
		 	np_dem[x][y]=35

#corremos el algoritmo de vecindad, si el 75% de los vecinos son negros entonces el punto (x,y) tambien lo sera
#esto lo hacemos unas 50 veces con una vecidad de radio 5

for x in xrange(1,5):
	gdal_dem = gdal.Open("/Users/meraioth/Desktop/dem_alig.tif",GA_Update);
	np_dem = np.array(gdal_dem.GetRasterBand(1).ReadAsArray())
	for x in xrange(np_dem.shape[0]):
	   for y in xrange(np_dem.shape[1]):
	       #print "punto"+str([x,y])
	       if np_dem[x][y]>=40.9 :
	           if vecindad(5,np_dem,[x,y])>75:
	               np_dem[x][y]=35
	gdal_dem.GetRasterBand(1).WriteArray(np_dem)
	print "paso"
	gdal_dem= None

gdal_dem = gdal.Open("/Users/meraioth/Desktop/dem_alig.tif",GA_Update);
np_dem = np.array(gdal_dem.GetRasterBand(1).ReadAsArray())

#Luego nuestro resultado lo pasamos a shp
ogr_ds = ogr.GetDriverByName("ESRI Shapefile").CreateDataSource(uri_lines)
contour_shp = ogr_ds.CreateLayer('contour')

field_defn = ogr.FieldDefn("ID", ogr.OFTInteger)
contour_shp.CreateField(field_defn)
field_defn = ogr.FieldDefn("elev", ogr.OFTReal)
contour_shp.CreateField(field_defn)

#Generate Contourlines
gdal.ContourGenerate(gdal_dem.GetRasterBand(1), 2, 0, [], 0, 0, contour_shp, 0, 1)
ogr_ds = None

#pasamos nuestro shp de lineas a poligonos
processing.runalg("qgis:linestopolygons",uri_lines,uri_polygons)
#anadimos informacion de area y perimetro a nuestra capa de poligonos
processing.runalg('qgis:exportaddgeometrycolumns', uri_polygons, 1 , uri_polygons2)
expression = '"area" > 5.99467533225426e-08'
#filtramos los edifcios menor a un area definida para eliminar ruido
processing.runandload('qgis:selectbyexpression', uri_polygons2, expression, 1)
processing.runandload('qgis:saveselectedfeatures', uri_polygons2, uri_final)

