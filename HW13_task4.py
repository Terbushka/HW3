from multiprocessing import Process, current_process, cpu_count
from concurrent.futures import ProcessPoolExecutor
import os


def print_cube(a):
    print(f"Process  id:{os.getpid()}, name {current_process().name}")
    return print(f'The cube number {a} = {a ** 3}')


def print_square(b):
    print(f"Process id:{os.getpid()}, name: {current_process().name}")
    return print(f'The square of number {b} = {b ** 2}')


print(f'Your CPU: {cpu_count()}')

with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(print_cube, 4)
    pool.submit(print_square, 6)

p1 = Process(name="print_cube", target=print_cube, args=(4,))
p2 = Process(name="print_square", target=print_square, args=(6,))
p1.start()
p2.start()