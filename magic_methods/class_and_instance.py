#!/usr/bin/env python3
#coding: utf-8

class A():
    b = 99
    def __init__(self):
        self.c = 10

    def show(self):
        print(self.b)


class B(A):
    pass



instance_a = []
instance_b = []

for i in range (0,10):
    instance_a.append(A())
    instance_b.append(B())

for i in instance_a:
    i.show()

#Меняем значение самого класса
A.b = 100

#Tут поменалось значение у всех экземпляров
for i in instance_a:
    i.show()

print()
#У наследников тоже поменялось значение
for i in instance_b:
    i.show()


class A():
    def __init__(self):
        print('A')
        super().__init__()

class B():
    def __init__(self):
        print('B')
        super().__init__()


class C(A,B):
    def __init__(self):
        print('C')
        super().__init__()


class D():
    def __init__(self):
        print('D')
        super().__init__()


class E():
    def __init__(self):
        print('E')
        super().__init__()                


class F(D, E):
    def __init__(self):
        print('F')
        super().__init__()        


class Z(C, F):
    def __init__(self):
        print('Z')
        super().__init__()

#help (Z)

# class A:
#     def who_am_i(self):
#         print("I am a A")

# class B(A):
#     def who_am_i(self):
#         print("I am a B")

# class C(A):
#     def who_am_i(self):
#         print("I am a C")

# class D(B,C):
#     def who_am_i(self):
#         print("I am a D")

# d1 = D()
# d1.who_am_i()


# help (D)

class Music(object): pass
class Rock(Music): pass
class Gothic(Music): pass
class Metal(Rock): pass
class GothicRock(Rock, Gothic): pass
class GothicMetal(Metal, Gothic): pass
class The69Eyes(GothicRock, GothicMetal): pass








help(The69Eyes)