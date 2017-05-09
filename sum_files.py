# -*- coding: utf-8 -*-
# Author:Guzhongren

# created: 2017-05-08
import os
filetype=[".JPG",".tif"]
folder_path = unicode(r"C:\geocon\解译样本（只提取jpg图片缩略图）", "utf8").encode("gbk")
jpg_count=0
tif_count=0
for parent, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        if filetype[0] in filename:
            jpg_count=jpg_count+1
        elif filetype[1] in filename:
            tif_count= tif_count+1
        else:
            a=0
print(u" jpg:"+ str(jpg_count)+u"  tif:"+ str(tif_count) + u"  sum:"+str(jpg_count+tif_count))
