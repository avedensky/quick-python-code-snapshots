#!/usr/bin/env python
#coding: utf-8
"""
	Switch in python
"""

def say_a():
	print('A')

def say_b():
	print('B')

def say_c():
	print('C')

def say_d():
	print('D')


def main():
	# switch in other language
	# for (int i=1; i<5; i++) {
	# 	switch (i) {
	# 		case 1:{
	# 		 	say_a();
	# 			break;
	# 		}
	#  		case 2:{
	# 			say_b();break;
	# 		}
	#  		case 3:{
	# 			say_c();break;
	# 		}
	#  		case 4:{
	# 			say_d();
	# 			break;
	# 		}
	# 	}
	# }

	# switch in python
	a = {1:say_a, 2:say_b, 3:say_c, 4:say_d}
	for i in range (1, 5):
		a[i]()


if __name__=='__main__':
	main()