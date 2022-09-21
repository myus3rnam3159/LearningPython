import os
from os import path
import shutil
from zipfile import ZipFile

#Lấy đường dẫn file
src = path.realpath("textfile.txt")

#copy file
dst = src + ".bak"
shutil.copy(src, dst)

#rename file
os.rename("textfile.txt", "newfile.txt")

#tạo file nén
root_dir, tail = path.split(src)
shutil.make_archive("archive", "zip", root_dir)

#thêm file vào zip
with ZipFile("testzip.zip", "w") as newzip:
    newzip.write("newfile.txt")
    newzip.write("textfile.txt.bak")