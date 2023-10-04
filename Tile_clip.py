import os
import numpy as np
from osgeo import gdal
import geopandas as gpd

rasterpath = "E:/Desktop/paper4/ModelInput_GEE/StasticData/China_stastic.tif"
# rasterpath = "E:/Desktop/paper4/ModelInput_GEE/StasticData/Terrain.tif"
# rasterpath = "E:/Desktop/paper4/ModelInput_GEE/MonthData/RSdata/RSApr.tif"

# rasterpath = "E:/Desktop/paper4/ModelInput_GEE/MonthData/Cmadata/CmaApr.tif"
# 将网格分成单个shp文件
gdpshp = gpd.read_file("E:/Desktop/paper4/shpdata/tile3.shp")
shpoutpath = "E:/Desktop/paper4/tile/tileshp/"
# for l in range(len(gdpshp)):
#     shp = gdpshp.iloc[l:l+1,:]
#     shp.to_file(shpoutpath+str(l)+".shp")


# outpath = "E:/Desktop/paper4/tile/raster/Month/RS/"
outpath = "E:/Desktop/paper4/tile/raster/stastic/"
# outpath = "E:/Desktop/paper4/tile/raster/terrain/"
shppath = shpoutpath
for shp in os.listdir(shppath):
    if (os.path.splitext(shp)[1] == ".shp"):
        dsT3 = gdal.Warp(outpath + 'stastic_' + os.path.splitext(shp)[0] + ".tif",  # 文件的输出路径及文件名
                         rasterpath,  # 拼接好的影像（待裁剪）
                         format='GTiff',  # 输出影像的格式
                         cutlineDSName=shppath+shp,
                         dstSRS='EPSG:4326',  # 参考：WGS84
                         cropToCutline=True,  # 将目标图像的范围指定为cutline 矢量图像的范围。
                         copyMetadata=True,
                         creationOptions=['COMPRESS=LZW', "TILED=True"],
                         dstNodata=np.nan)


