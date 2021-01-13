from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)


if __name__ == '__main':
    processes = []
    num_processes = os.cpu_count()

    # create processes and assign a function for each process
    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    # start all processes
    for p in processes:
        p.start()

    # wait for all processes to finish
    # block the main program until these processes are finished
    for p in processes:
        p.join()

    print('end main')
