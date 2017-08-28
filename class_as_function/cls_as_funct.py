#!/usr/bin/env python3
#coding: utf-8

"""
Call instance of class as function
"""


class calc():
    def __init__(self, *args, **kwargs):
        self.some_value = 20

    def start(self):
        print('start')

    def end(self):
        print('end')

    def __call__(self, value):
        self.start()
        res = self.some_value * value
        self.end()        
        return res


def main():
    instance = calc()
    print(instance(10))

    my_function = instance
    print(my_function(20))


if __name__=='__main__':
    main()


        