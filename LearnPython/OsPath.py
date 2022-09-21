from datetime import datetime
import os
from os import path
import time


#In ra tên hệ điều hành
print(os.name)

#Kiểm tra file có tồn tại không
path.exists("textfile.txt")
#Kiểm tra là file hay là folder
path.isfile("textfile.txt")
path.isdir("textfile.txt")

#Lấy path của file
path.realpath("textfile.txt")

#Lầy thời gian chỉnh sửa
# Convert giây sang thời gian kiểu string
t = time.ctime(path.getmtime("textfile.txt"))
print(t)
print(datetime.fromtimestamp(path.getmtime("textfile.txt")))

path.abspath()