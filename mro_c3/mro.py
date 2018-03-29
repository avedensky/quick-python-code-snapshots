#!/usr/bin/env python3
#coding: utf-8

'''

This short sample is show, how worked MRO C3 algoritm.

In this sample:
Method resolution order(MRO C3): D,C,B,A
For show MRO order, may use help(our_class) or print (D.__mro__)

'''

class A():
	def say(self):
		print("A")


class B(A):
	def say(self):
		print("B")


class C(A):
	def say(self):
		print("C")
		super().say() #here is magic MRO. Call B.say() will be done.


class D(C, B):
	def call_say(self):
		super().say()


def main():
	d=D()
	d.say()
	print(D.__mro__)
	print(D.__bases__)


if __name__=='__main__':
	main()