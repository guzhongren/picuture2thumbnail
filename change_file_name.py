# -*- coding: utf-8 -*-
# Author:Guzhongren

# created: 2017-05-08
import os
path = 'C:\\geoconFailed\\willfix\\'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        _file= file.split(".")
        _file_name=_file[0]
        _file_type=_file[1]
        new_file_name=_file_name[:-1]+"."+_file_type
        os.rename(os.path.join(path,file), os.path.join(path, new_file_name))
        print(file+u"更名成功")

