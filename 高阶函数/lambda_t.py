# -*- coding: utf-8 -*-
# @File    : test_lambda.py
# @Software: PyCharm
'''
匿名函数，简化写法，不能有 print if
'''

#单个参数
g = lambda x:x+1
print(g(3))

#多个参数
g = lambda x,y,z:(x+y)**z
print(g(1,2,3))

#list
g = [lambda x,y:x+y,lambda y:y+2]
print(g[0](3,6))
