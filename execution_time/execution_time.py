#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
"""

Measuring the execution time of the function

"""


def execution_time(fn):
    def wrapper():
        start_time = time.time()
        fn()
        end_time = time.time()
        delta_time = end_time - start_time
        print ("\n------------------")
        print ("Function (%s) lead time: %s seconds" % (fn.__name__, str(delta_time)))

    return wrapper


@execution_time
def calculate():
    print (9**9**6)


def main():
    calculate()


if __name__=="__main__":
    main()
