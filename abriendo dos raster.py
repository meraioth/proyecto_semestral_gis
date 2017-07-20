#abriendo dos
from __future__ import division
#uri de capa activa
uri_ndvi=iface.activeLayer().dataProvider().dataSourceUri()

gdal_ndvi = gdal.Open("/Users/meraioth/Desktop/NDVI.tif")
gdal_dem = gdal.Open("/Users/meraioth/Desktop/dem_alig.tif");

np_ndvi = np.array(gdal_ndvi.GetRasterBand(1).ReadAsArray())
np_dem = np.array(gdal_dem.GetRasterBand(1).ReadAsArray())

count = 0
total_terreno = 0

for x in xrange(np_ndvi.shape[0]):
	for y in xrange(np_ndvi.shape[1]):
         if np_ndvi[x][y]> -1 and np_ndvi[x][y] < 1:
            total_terreno+=1
            if np_ndvi[x][y]>0.2:
                count+=1
                np_dem[x][y]=35
                
                

 


print str(100*count/total_terreno)+"%"



from __future__ import division
#uri de capa activa
uri_ndvi=iface.activeLayer().dataProvider().dataSourceUri()

gdal_ndvi = gdal.Open("/Users/meraioth/Desktop/NDVI.tif")
gdal_dem = gdal.Open("/Users/meraioth/Desktop/dem_alig.tif",GA_Update);

np_ndvi = np.array(gdal_ndvi.GetRasterBand(1).ReadAsArray())
np_dem = np.array(gdal_dem.GetRasterBand(1).ReadAsArray())

count = 0
total_terreno = 0
driver = gdal_dem.GetDriver()

for x in xrange(np_dem.shape[0]):
	for y in xrange(np_dem.shape[1]):
         if np_dem[x][y]<40.5 :
            np_dem[x][y]=35
                
                

 




gdal_dem.GetRasterBand(1).WriteArray(np_dem)
print "paso"
gdal_dem= None