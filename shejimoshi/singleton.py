# -*- coding: utf-8 -*-
# @File    : singleton.py
# @Software: PyCharm

'''
单例模式，保证只有一个实例
'''

import threading

#线程安全
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self,name):
        self.name = name

a = MyClass('a')
b = MyClass('b')
print(a.name)  #b
print(b.name)  #b


#单例装饰器
from functools import wraps

def Singleton(cls):
    _instance = {}
    @wraps(cls)
    def _singlenton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singlenton

@Singleton
class MyClassDecotor():
    def __init__(self,name):
        self.name = name


#测试多线程
def test_thread():
    a = MyClassDecotor('a')
    print(id(a))

for i in range(100):
    t = threading.Thread(target=test_thread,)
    t.start()





