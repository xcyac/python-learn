# -*- coding: utf-8 -*-
# @File    : strategy.py
# @Software: PyCharm


'''
策略模式
        上下文（content）
        抽象策略  (Comparable)
        具体策略  (Cpmparetor)
优点：
    1.定义了一系列可重用的算法和行为
    2.消除了一些条件语句
    3.可以提供相同行为的不同实现
缺点:
    1.必须了解不用的策略
'''

from abc import ABCMeta,abstractmethod


class Strategy(metaclass=ABCMeta):

    @abstractmethod
    def exectue(self,data):
        pass

class OneStrategy(Strategy):

    def exectue(self,data):
        print("策略一具体实现:%s"%data)

class TwoStrategy(Strategy):
    def exectue(self,data):
        print("策略二具体实现:%s"%data)



class Content():
    def __init__(self,strategy,data):
        self.strategy = strategy
        self.data = data

    def set_strategy(self,strategy):
        self.strategy = strategy

    def do(self):
        self.strategy.exectue(self.data)



if __name__ == "__main__":
    one = OneStrategy()
    two = TwoStrategy()
    c = Content(one,[''''''])
    c.do()
    c.set_strategy(two)
    c.do()