#!/usr/local/bin/python3

import sys
import math
import json
import time
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

#print("Hello, Python3!")

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
# 成员测试
if ('Rose' in student):
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号 
这是多行注释，用三个单引号
'''

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x)


# 定义函数
def printme(str):
    print(str)
    return
# 调用函数
printme("我要调用用户自定义函数!")

f = open("/tmp/foo.txt", "w")
f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# 关闭打开的文件
f.close()

a=math.cos(math.pi / 4)
print(a)

# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_str = json.dumps(data)
print ("JSON 对象：", json_str)

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
