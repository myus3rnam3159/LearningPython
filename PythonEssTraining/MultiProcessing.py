from multiprocessing import Process
import time

def longSquare(num, results):
    time.sleep(1)
    print(num ** 2)



if __name__ == '__main__':
    results = {}
    p1 = Process(target=longSquare, args=(1,results))
    p2 = Process(target=longSquare, args=(2,results))

    #Chạy process
    p1.start()
    p2.start()

    #Đợi cho process dừng
    p1.join()
    p2.join()

    #Process chạy // nhưng dừng hết mới print
    print(results)