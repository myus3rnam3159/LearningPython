#Tách string
text = "hflshflsf rwrwrer ưerrwwerqr"
text.split()

# Xem biến, code trong function
def x():
    return 5
x.__code__.co_varnames
x.__code__.co_code

#Phương thức cá thể hàm có self parameter trong class
#Phương thức tĩnh là hàm bình thường

#Kiểu dữ liệu bytes

# dài 4 bytes
bytes(4)

# encode sử dụng byte
smileyBytes = bytes('🏀', 'utf-8')
#decode
smileyBytes.decode('utf-8')
#gán giá trị cho một phần tử mảng byte bằng 85 trong hệ 16
smileyBytes[3] = int('85', 16)

#kế thừa: https://www.w3schools.com/python/python_inheritance.asp
class UniqueList(list):
    def __init__(self):
        super.__init__()
    def append(self, __object: _T) -> None:
        return super().append(__object)

#Customer Exception
class CustomException(Exception):
    pass