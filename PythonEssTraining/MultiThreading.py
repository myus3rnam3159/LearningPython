from json import load
import threading
import time

#Ví dụ một hàm
def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2

results = {}

#Tạo 2 luồng
t1 = threading.Thread(target=longSquare, args = (1, results))
t2 = threading.Thread(target=longSquare, args=(2, results))

#Chạy luồng cùng tác động vào bộ nhớ cho chỉ 1 quá trình chạy hàm longsquare
t1.start()
t2.start()

#đợi khi nào luồng 1 kết thúc
t1.join()
#đợi luồng 2 kết thúc
t2.join()

#Luồng chạy // nhưng dừng hết mới print

print(results)