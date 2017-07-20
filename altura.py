#script para calcular cantidad de vegetación en %
from __future__ import division
import osr
import os
import structure

#se obtiene capa actual
layer1 = iface.mapCanvas().layer(0)
layer1.name()
import numpy as np
from osgeo import gdal
provider=layer1.dataProvider()
filePath = str(provider.dataSourceUri())
print filePath
#se abre el archivo con gdal desde la ruta de nuestra capa seleccionada
ds = gdal.Open(filePath)
#se transforma en un numpy array
myarray = np.array(ds.GetRasterBand(1).ReadAsArray())
count = 0
total_terreno = 0
# se itera en forma de matriz, contando las casillas validas y contando
#las casillas que tengan un NDVI mayor a 0.2 

for x in xrange(myarray.shape[0]):
	for y in xrange(myarray.shape[1]):
         if myarray[x][y]> 35.8187 and myarray[x][y] < 72.0223:
            if myarray[x][y]<40:
                myarray[x][y]=60



raster = np.asarray(myarray)

#Get raster metadata
geotransform = dataset.GetGeoTransform()

# Set name of output raster
output_file = "/Users/meraioth/Desktop/raster_output.tif"

# Create gtif file with rows and columns from parent raster 
driver = gdal.GetDriverByName("GTiff")

raster = changeRasterValues(band)

dst_ds = driver.Create(output_file, 
                       band.XSize, 
                       band.YSize, 
                       number_band, 
                       band.DataType)

#writting output raster
dst_ds.GetRasterBand(number_band).WriteArray( raster )

#setting extension of output raster
# top left x, w-e pixel resolution, rotation, top left y, rotation, n-s pixel resolution
dst_ds.SetGeoTransform(geotransform)

# setting spatial reference of output raster 
srs = osr.SpatialReference(wkt = prj)
dst_ds.SetProjection( srs.ExportToWkt() )

#Close output raster dataset 
dst_ds = None

#Close main raster dataset
dataset = None
 
