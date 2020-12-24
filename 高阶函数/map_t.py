# -*- coding: utf-8 -*-
# @File    : map_t.py
# @Software: PyCharm

'''
map
'''

g = map(lambda x,y:x+y,[2,3],[4,6])
for i in g:
    print(i)

#参数类型不一致会报错
g = map(lambda x,y:x+y,[2,3],[4,'6'])
for i in g:
    print(i)

#参数个数不足时，有几个处理几个
g = map(lambda x,y:x+y,[2,3],[4])
for i in g:
    print(i)