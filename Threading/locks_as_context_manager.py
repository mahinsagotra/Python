# import Lock
from threading import Thread, Lock
import time


database_value = 0


def increase(lock):
    global database_value

    # lock as a context manager
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":

    # create a lock
    lock = Lock()

    print('Start value: ', database_value)

    # pass the lock to the target function
    # notice the comma after lock since args must be a tuple
    t1 = Thread(target=increase, args=(lock,))
    t2 = Thread(target=increase, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')
