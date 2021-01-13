from threading import Thread, local
import time

database_value = 0


def increase():
    global database_value

    local_value = database_value

    # processing
    local_value += 1
    time.sleep(0.1)
    database_value = local_value


if __name__ == "__main__":
    print(f'start value {database_value}')

    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end Value', database_value)

    print('end main')
