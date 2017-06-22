#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Connect to http://www.ripn.net/nic/whois/whois.cgi and get html page with parametrs

import urllib
import urllib2





#proxys = "192.168.23.4:8080" # в формате прокси:порт
#user = "login" # прокси логин
#password = "password" # прокси пароль



#proxy = urllib2.ProxyHandler({"http" : proxys}) #инициализация 
# - пока не нужно -    proxy_auth_handler = urllib2.ProxyBasicAuthHandler() # инициализация авторизации в прокси
# - пока не нужно -    proxy_auth_handler.add_password('realm', 'uri', user, password) # добавляем логин и пароль в прокси

# собираем загрузчик прокси, авторизации и кукилиба
#opener = urllib2.build_opener(proxy,здесь еще handler ntlm авторизации должен быть)
#urllib2.install_opener(opener) # устанавливаем загрузчик



headers = {'User­Agent' : 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
values = {'Host' : 'whois.ripn.net', 'Whois' : 'ya.ru'}
data = urllib.urlencode(values) #преобразовывает текст в строку key=value&key=value


req = urllib2.Request('http://www.ripn.net/nic/whois/whois.cgi', data, headers)
#response = opener.open(req)
response = urllib2.urlopen(req)
print response.read()
