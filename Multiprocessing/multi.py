from multiprocessing import Process, Value, Array, Lock
import os
import time


def add_100(number, lock):
    for i in range(100):
        with lock:
            time.sleep(0.01)
            number.value += 1


def add_100_array(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1


if __name__ == '__main__':

    lock = Lock()

    shared_number = Value('i', 0)
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Number at beginning is', shared_number.value)
    print('Array at beginning is', shared_array[:])

    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))

    p3 = Process(target=add_100_array, args=(shared_array, lock))
    p4 = Process(target=add_100_array, args=(shared_array, lock))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print('number at end is', shared_number.value)
    print('number at end is', shared_array[:])

    print('end main')
