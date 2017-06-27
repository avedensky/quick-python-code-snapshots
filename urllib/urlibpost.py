#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Connect to http://www.ripn.net/nic/whois/whois.cgi and get html page with parametrs by POST Method

import urllib
import urllib2

headers = {'User­Agent' : 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
values = {'Host' : 'whois.ripn.net', 'Whois' : 'ya.ru'}
data = urllib.urlencode(values) #преобразовывает текст в строку key=value&key=value


req = urllib2.Request('http://www.ripn.net/nic/whois/whois.cgi', data, headers)
response = urllib2.urlopen(req)
print response.read()
