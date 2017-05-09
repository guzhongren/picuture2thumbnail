# -*- coding: utf-8 -*-
# Author:Guzhongren

# created: 2017-04-28
import os
import sys
import arcpy
from PIL import Image
reload(sys)
sys.setdefaultencoding("utf-8")

# tif 4波段图像转换为3波段图像   --未用
def band4_2_band3_raster(band4_raster_path, temp_file_path):
    raster_arr = arcpy.RasterToNumPyArray(
        band4_raster_path.decode("utf8").encode("gbk"))
    raster_arr_3d = raster_arr[:3, :, :]
    print(band4_raster_path + "ssss")
    path_pices = band4_raster_path.split("\\")
    file_name = path_pices[len(path_pices) - 1].split(".")[0]

    new_raster = arcpy.NumPyArrayToRaster(raster_arr_3d)
    new_raster.save(temp_file_path + "\\" + file_name + ".tif")
    del raster_arr, raster_arr_3d, new_raster
    return temp_file_path


# 获取影像的波段数
def getband_count(input_raster_path):
    raster = arcpy.Raster(input_raster_path)
    print(u"获取的波段数:" + str(raster.bandCount))
    return raster.bandCount
# 生成tif的缩略图


def generate_tif_thumbnail(input_raster_path, target_path):
    print u"开始生成tif " + input_raster_path + u" 的缩略图......"
    img = Image.open(input_raster_path)
    region = img.crop((0, 0, 380, 380))
    #img.thumbnail(img.size, Image.ANTIALIAS)
    # img.save(target_path + img.filename.split(parent)
    #         [1].split(".")[0] + ".jpeg", "JPEG")
    path_pices = img.filename.split("\\")
    file_name = path_pices[len(path_pices) - 1].split(".")[0]
    region.save(target_path + "\\" + file_name + ".jpg", "JPEG")
    del path_pices, file_name,region
    print u"成功，生成"+img.filename+"..."
    del img


# 生成jpg图像的缩略图  raster_path必须为3波段的影像或者jpg
def generate_thumbnail(input_raster_path, target_path):
    print u"开始生成" + input_raster_path + u" 的缩略图......"
    img = Image.open(input_raster_path)
    img.thumbnail(img.size, Image.ANTIALIAS)
    # img.save(target_path + img.filename.split(parent)
    #         [1].split(".")[0] + ".jpeg", "JPEG")
    path_pices = img.filename.split("\\")
    file_name = path_pices[len(path_pices) - 1].split(".")[0]
    img.save(target_path + "\\" + file_name + ".jpg", "JPEG")
    del path_pices, file_name
    print u"成功，生成"+img.filename+"..."
    del img


def for_each_file(folder_path, target_path):
    try:
        for parent, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(
                    parent.decode("gbk"), filename.decode("gbk"))
                if img_type[0] in filename:
                    generate_thumbnail(file_path, target_path)
                #elif img_type[1] in filename:
                    #generate_tif_thumbnail(file_path, target_path)
                else:
                    print(u"未知类型的数据不能生成缩略图")
    except Exception, e:
        print e


if __name__ == "__main__":
    # 图片存放目录
    folder_path = unicode(r"C:\geocon\解译样本（只提取jpg图片缩略图）", "utf8").encode("gbk")
    target_path = unicode(r"C:\geocon\thumbile", "utf8").encode("gbk")
    img_type = [".jpg", ".tif"]  # 过滤类型
    for_each_file(folder_path, target_path)
