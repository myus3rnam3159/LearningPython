#Mở file để ghi, có thể tạo mới nếu chưa tồn tại
file = open("textfile.txt", "w+")
file.write("This is some text \n")
file.close()

#Đọc file
file = open("textfile.txt", "r")
content = file.read()
#Đọc file vô list
fl = file.readlines()

for l in fl:
    print(l)