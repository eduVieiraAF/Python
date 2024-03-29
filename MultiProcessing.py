# ? Multiprocessing = running thread in parallel on different CPU core, bypasses GIL and is used for threading
# ? multiprocessing → better for cpu bound tasks (heavy cpu usage)
# ? multithreading → better for io bound tasks (waiting around)

import time
from multiprocessing import Process, cpu_count


def counter(num):
    count = 0

    while count < num:
        count += 1


def main():
    print(cpu_count())

    a = Process(target=counter, args=(500000,))  # comma to differentiate from expression
    b = Process(target=counter, args=(500000,))  # comma to differentiate from expression

    a.start()
    b.start()

    a.join()  # Process synchronization
    b.join()  # Process synchronization

    print("Finished in:", time.perf_counter(),
          "seconds")  # to see how they'll work in parallel add more or remove Processes


if __name__ == '__main__':
    main()
