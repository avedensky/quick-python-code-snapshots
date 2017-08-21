#!/usr/bin/env python3
#coding: utf-8

"""

	Check ping (linux)
	Ping host and return dictionary values of ping: min,avg,max,mdev

"""
from subprocess import Popen, PIPE


def get_ping_values(host):
	"""
	The function ping host and return dictionary values of ping: min,avg,max,mdev
	"""
	cmd = 'ping -q -c5 {0} | tail -n 1 | grep \'rtt\''.format(host)
	p = Popen([cmd], shell=True, stdout=PIPE)
	s = p.stdout.read().decode("utf-8")

	if s=='': #host is not find
		return {}

	keys = s[4:20].split(r'/')
	values = s[23:46].split(r'/')
	
	return dict(zip(keys, values))
	

#for test
if __name__=='__main__':
	print("Test\n127.0.0.1: You can see some values:")
	print(get_ping_values('127.0.0.1'))
	print("\n240.0.0.0: You can see empty dictionary:")
	print(get_ping_values('240.0.0.0'))
	