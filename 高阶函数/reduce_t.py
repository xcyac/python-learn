# -*- coding: utf-8 -*-
# @File    : reduce_t.py
# @Software: PyCharm

from functools import reduce

'''
无初始值
执行过程:
    1+2=3
    3+3=6
'''
g = reduce(lambda x,y:x+y,[1,2,3])
print(g)

'''
有初始值:
    5+1=6
    6+2=8
    8+3=11
'''
g = reduce(lambda x,y:x+y,[1,2,3],5)
print(g)
