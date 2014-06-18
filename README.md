sca
===

Snow cover assessment tool using Python


Dependencies
===

+ Python 2.7.x
+ PyQt4 / PySide
+ GDAL
+ Numpy
+ Matplotlib


Authors
===

Antara (antaradasgupta26@gmail.com)

Prasun (@pkg_sd)


Version
===

1.0 - April 25, 2014


Inputs
===

+ Directory path containing pre-extracted TIFF files of MODIS MOD10A2-L8 (8-day composite) data. Subdataset used was of the Maximum Snow Extent over the 8 day period.


+ HDF to GeoTIFF conversion can be done in many ways
    - [HDF-EOS to GeoTIFF Conversion Tool (HEG)](http://hdfeos.org/software/heg.php)
    - [Online MODIS Reprojection Tool](https://lpdaac.usgs.gov/tools/modis_reprojection_tool)
    - [Using Extract Subdataset (Data Management) in ArcGIS Help 10.1](http://resources.arcgis.com/en/help/main/10.1/index.html#//00170000009s000000)
    - For the **brave-hearted** [GDAL_TRANSLATE](http://www.gdal.org/gdal_translate.html)


Outputs
===

+ Graph showing changes in snow cover area over the given period


Slideshow
===
Available on [this link](http://www.slideshare.net/prasun001/snow-cover-assessment-tool-using-python) 
