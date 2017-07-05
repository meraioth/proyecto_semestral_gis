#script para calcular cantidad de vegetación en %
from __future__ import division
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
         if myarray[x][y]> -1 and myarray[x][y] < 1:
            total_terreno+=1
            if myarray[x][y]>0.2:
                count+=1
 
print str(100*count/total_terreno)+"%"
