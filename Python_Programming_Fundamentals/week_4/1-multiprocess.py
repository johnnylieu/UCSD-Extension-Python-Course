"""Write a Python multiprocessing program that runs all five functions below. 
Use a time.counter to tests the amount of time it takes all functions to run synchronously and then concurrently
 

def add(x, y):

    time.sleep(1)

    return x + y

def subtract(x, y):

   time.sleep(1)
    return x-y

def multiply(x, y):

   time.sleep(1)
    return x * y

def divide(x, y):

    time.sleep(1)
    if y==0:
        raise ValueError('Cannot divide by zero!')
    return x / y

def modulus(x, y):

    time.sleep(1)
    return x % y"""

import multiprocessing
import time

def add(x, y):

    time.sleep(1)

    return x + y

def subtract(x, y):

   time.sleep(1)
   return x-y

def multiply(x, y):

   time.sleep(1)
   return x * y

def divide(x, y):

    time.sleep(1)
    if y==0:
        raise ValueError('Cannot divide by zero!')
    return x / y

def modulus(x, y):

    time.sleep(1)
    return x % y


if __name__ == "__main__":
    # concurrently
    concurrent_start = time.perf_counter()
    add(6, 2)
    subtract(6, 2)
    multiply(6, 2)
    divide(6, 2)
    modulus(6, 2)
    concurrent_finish = time.perf_counter()
    print(f"Concurrent execution time: {concurrent_finish - concurrent_start} seconds.")

    # syncrhonously
    synch_start = time.perf_counter()
    process1 = multiprocessing.Process(target=add, args=(2, 6))
    process2 = multiprocessing.Process(target=subtract, args=(2, 6))
    process3 = multiprocessing.Process(target=multiply, args=(2, 6))
    process4 = multiprocessing.Process(target=divide, args=(2, 6))
    process5 = multiprocessing.Process(target=modulus, args=(2, 6))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()

    synch_finish = time.perf_counter()
    print(f"Sychronous execution time: {synch_finish - synch_start} seconds.")