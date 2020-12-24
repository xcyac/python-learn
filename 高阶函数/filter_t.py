# -*- coding: utf-8 -*-
# @File    : filter_t.py
# @Software: PyCharm

'''
filter  过滤
'''

g = filter(lambda x:x<5,[1,2,3,4,5])
print(g,type(g))
for i in g:
    print(i)