from timing import time_function
from datetime import datetime
import tokenize



@time_function
def do_stuff():
    for i in range(100):
        if i % 25 == 0:
            print(i)
        for j in range(100):
            if j % 25 == 0:
                print(j)
    return "Hello"

do_stuff()
