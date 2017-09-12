#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Example of socket and multiprocessing
----------------

The program open socket and listen PORT

Every connected clients is processed by a separate process

For check from client use linux utility netcat, for example:
netcat -v localhost 9012
the next, you can writin in terminal

"""

import socket
import sys
from multiprocessing import Process

HOST = '' #  c любых адресов
PORT = 9012
CLIENTS_LIMIT = 5 # макс колличество соединений
DATA_BUFFER = 1024


# SOCK_STREAM надёжная потокоориентированная служба (TCP)
# AF_INET для сетевого протокола IPv4

# SOL_SOCKET Уровень библиотеки сокетов для. Далее установка параметров 
# для этого уровня 
# SO_REUSEADDR Разрешает повторное использование локальных адресов 
# (если данная возможность поддерживается используемым протоколом). 
# Параметр имеет логическое значение.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(CLIENTS_LIMIT)


def worker(connection, dest_addr):        
    try:    
        data = b''
        while True:
            data = connection.recv (DATA_BUFFER)                        
            sys.stdout.flush()
            if len(data)==0:
                print('No data, exit from woker')
                return
            else:
                print('Recived data from: {0}; Data: {1}'.format(dest_addr, data))
    except KeyboardInterrupt:
        return


def run_server():
    try:
        while True:
            conn, addr = server.accept() 

            print('Connect from {0}'.format(addr))
            sys.stdout.flush()

            process = Process(target=worker, args=(conn, addr,))
            process.start()                    

    except KeyboardInterrupt:
        server.close()        

    finally:
        server.close()



if __name__=='__main__':
    run_server()


# Other Options for socket
# SO_DEBUG
# Включить запись отладочной информации. Параметр имеет логическое значение.
# SO_BROADCAST
# Разрешить отправку широковещательных пакетов (если данная возможность поддерживается используемым протоколом). Параметр имеет логическое значение.
# SO_REUSEADDR
# Разрешает повторное использование локальных адресов (если данная возможность поддерживается используемым протоколом). Параметр имеет логическое значение.
# SO_KEEPALIVE
# Сохраняет установленные соединения путем периодической передачи сообщений (если данная возможность поддерживается используемым протоколом). Если удаленный сокет не отвечает на сообщение, то соединение считается разорванным, процессу, осуществляющему запись в сокет, посылается сигнал SIGPIPE. Параметр имеет логическое значение.
# SO_SNDBUF
# Устанавливает размер буфера отправки. Параметр имеет целое значение.
# SO_RCVBUF
# Устанавливает размер буфера приема сообщений. Параметр имеет целое значение.
# SO_SNDTIMEO
# Устанавливает максимальный интервал времени в течение которого функция вывода ждет завершения. Если функция, отправляющая данные, не завершается в течение указанного интервала, то она либо возвращает частичный ответ, либо, если данные отправлены не были, присваивает переменной errno значение EAGAIN или EWOULDBLOCK. По умолчанию параметр равен нулю, что означает отсутствие таймаута. Параметру присваивается значение типа struct timeval.
# SO_RCVTIMEO
# Параметр аналогичен предыдущему, но устанавливает таймаут для функций ввода.
# На уровне протокола TCP допустимы следующие параметры:

# TCP_NODELAY
# Не задерживать отправку данных. Если данный параметр установлен, то отключается алгоритм буферизации. Параметр имеет логическое значение.
# TCP_MAXSEG
# Устанавливает максимальный размер сегмента данных. Параметр имеет целое значение.
# TCP_NOPUSH
# Не использовать проталкивание. Параметр имеет логическое значение.
# TCP_NOOPT
# Не использовать параметры TCP. Параметр имеет логическое значение.
# Параметры имеющие логическое значение являются целыми. Значение 0 обозначает, что соответствующий параметр будет отключен, значение 1 обозначает, что параметр будет включен. В случае успешного завершения функция фозвращает ноль, если возникли ошибки, то результат равен -1.

# Функция getsockopt возвращает значение указанного параметра. Помимо вышеперечисленных параметров могут использоваться следующие:

# SO_ERROR
# Возвращает информацию о коде ошибки. Параметр имеет целое значение.
# SO_TYPE
# Возвращает тип сокета. Параметр имеет целое значение.

