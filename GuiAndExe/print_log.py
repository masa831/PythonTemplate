#-*- coding:utf-8 -*-
import sys
from time import sleep

def count_up(num, count):
    print("--- start ----")

    for i in range(0, count):
        print(num + i)
        sleep(0.5)

    print("--- end ----")

if __name__ == '__main__':
    count_up(1, 10)