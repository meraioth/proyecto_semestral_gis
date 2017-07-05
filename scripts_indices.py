from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

chLayer = qgis.utils.iface.activeLayer()

entries = []

ch1 = QgsRasterCalculatorEntry()
ch1.ref = 'chillan@1'
ch1.raster = chLayer
ch1.bandNumber = 1
entries.append(ch1)

ch4 = QgsRasterCalculatorEntry()
ch4.ref = 'chillan@4'
ch4.raster = chLayer
ch4.bandNumber = 4
entries.append(ch4)

calc = QgsRasterCalculator(
	'( ( chillan@4 - chillan@1 ) / ( chillan@4 + chillan@1 ) )',
	'/Users/meraioth/Desktop/GNNDVI.tif',
	'GTiff',
	chLayer.extent(),
	chLayer.width(),
	chLayer.height(),
	entries
)
print calc.processCalculation()




from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

chLayer = qgis.utils.iface.activeLayer()

entries = []

ch3 = QgsRasterCalculatorEntry()
ch3.ref = 'chillan@3'
ch3.raster = chLayer
ch3.bandNumber = 3
entries.append(ch3)

ch4 = QgsRasterCalculatorEntry()
ch4.ref = 'chillan@4'
ch4.raster = chLayer
ch4.bandNumber = 4
entries.append(ch4)

calc = QgsRasterCalculator(
	'( ( chillan@4 - chillan@3 ) / ( chillan@4 + chillan@3 ) )',
	'/Users/meraioth/Desktop/NDRE.tif',
	'GTiff',
	chLayer.extent(),
	chLayer.width(),
	chLayer.height(),
	entries
)
print calc.processCalculation()


from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

chLayer = qgis.utils.iface.activeLayer()

entries = []

ch2 = QgsRasterCalculatorEntry()
ch2.ref = 'chillan@2'
ch2.raster = chLayer
ch2.bandNumber = 2
entries.append(ch2)

ch4 = QgsRasterCalculatorEntry()
ch4.ref = 'chillan@4'
ch4.raster = chLayer
ch4.bandNumber = 4
entries.append(ch4)

calc = QgsRasterCalculator(
	'( ( chillan@4 - chillan@2 ) / ( chillan@4 + chillan@2 ) )',
	'/Users/meraioth/Desktop/NDVI.tif',
	'GTiff',
	chLayer.extent(),
	chLayer.width(),
	chLayer.height(),
	entries
)
print calc.processCalculation()

from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

chLayer = qgis.utils.iface.activeLayer()

entries = []

ch1 = QgsRasterCalculatorEntry()
ch1.ref = 'chillan@1'
ch1.raster = chLayer
ch1.bandNumber = 1
entries.append(ch1)

ch4 = QgsRasterCalculatorEntry()
ch4.ref = 'chillan@4'
ch4.raster = chLayer
ch4.bandNumber = 4
entries.append(ch4)

calc = QgsRasterCalculator(
	'( ( chillan@4  ) / ( chillan@1  ) )',
	'/Users/meraioth/Desktop/GRVI.tif',
	'GTiff',
	chLayer.extent(),
	chLayer.width(),
	chLayer.height(),
	entries
)
print calc.processCalculation()


# from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

# chLayer = qgis.utils.iface.activeLayer()

# entries = []

# ch1 = QgsRasterCalculatorEntry()
# ch1.ref = 'conce@1'
# ch1.raster = chLayer
# ch1.bandNumber = 1
# entries.append(ch1)

# ch4 = QgsRasterCalculatorEntry()
# ch4.ref = 'conce@4'
# ch4.raster = chLayer
# ch4.bandNumber = 4
# entries.append(ch4)

# calc = QgsRasterCalculator(
# 	'( ( conce@4 - conce@1 ) / ( conce@4 + conce@1 ) )',
# 	'/Users/meraioth/Desktop/GNNDVI.tif',
# 	'GTiff',
# 	chLayer.extent(),
# 	chLayer.width(),
# 	chLayer.height(),
# 	entries
# )
# print calc.processCalculation()




# from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

# chLayer = qgis.utils.iface.activeLayer()

# entries = []

# ch3 = QgsRasterCalculatorEntry()
# ch3.ref = 'conce@3'
# ch3.raster = chLayer
# ch3.bandNumber = 3
# entries.append(ch3)

# ch4 = QgsRasterCalculatorEntry()
# ch4.ref = 'conce@4'
# ch4.raster = chLayer
# ch4.bandNumber = 4
# entries.append(ch4)

# calc = QgsRasterCalculator(
# 	'( ( conce@4 - conce@3 ) / ( conce@4 + conce@3 ) )',
# 	'/Users/meraioth/Desktop/NDRE.tif',
# 	'GTiff',
# 	chLayer.extent(),
# 	chLayer.width(),
# 	chLayer.height(),
# 	entries
# )
# print calc.processCalculation()


# from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

# chLayer = qgis.utils.iface.activeLayer()

# entries = []

# ch2 = QgsRasterCalculatorEntry()
# ch2.ref = 'conce@2'
# ch2.raster = chLayer
# ch2.bandNumber = 2
# entries.append(ch2)

# ch4 = QgsRasterCalculatorEntry()
# ch4.ref = 'conce@4'
# ch4.raster = chLayer
# ch4.bandNumber = 4
# entries.append(ch4)

# calc = QgsRasterCalculator(
# 	'( ( conce@4 - conce@2 ) / ( conce@4 + conce@2 ) )',
# 	'/Users/meraioth/Desktop/NDVI.tif',
# 	'GTiff',
# 	chLayer.extent(),
# 	chLayer.width(),
# 	chLayer.height(),
# 	entries
# )
# print calc.processCalculation()

# from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

# chLayer = qgis.utils.iface.activeLayer()

# entries = []

# ch1 = QgsRasterCalculatorEntry()
# ch1.ref = 'conce@1'
# ch1.raster = chLayer
# ch1.bandNumber = 1
# entries.append(ch1)

# ch4 = QgsRasterCalculatorEntry()
# ch4.ref = 'conce@4'
# ch4.raster = chLayer
# ch4.bandNumber = 4
# entries.append(ch4)

# calc = QgsRasterCalculator(
# 	'( ( conce@4  ) / ( conce@1  ) )',
# 	'/Users/meraioth/Desktop/GRVI.tif',
# 	'GTiff',
# 	chLayer.extent(),
# 	chLayer.width(),
# 	chLayer.height(),
# 	entries
# )
# print calc.processCalculation()







