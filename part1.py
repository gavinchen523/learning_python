#!/usr/bin/env python

# print
print('hello world')

# Variable
a=123
print(type(a))
b='456'
print(type(b))
c=4.123
print(type(c))
a=5
b=8
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #無條件捨去除法
print(a**b) #a 的 b次方
a=-3
b=4
print(abs(a)) #絕對值
print(max(a,b)) #最大值
print(min(a,b)) #最小值
a=123
b='456' #str
print(a+int(b)) 
print(str(a)+b) #str

# Input
a=input() #不會有提示，而且a為字串的型態
print('a = ', a)
b=input('Your name: ')
print('Your name: ', b)

# if-else
# > < >= <= == != true false and or not 
battery = 20
if battery > 80:
    print('>80')
elif battery < 30:
    print('<30')
else:
    print ('80 >= battery >= 30')

# for loop
# range(n)=range(0,n)
# range(起點，絡點，間距)
#for i in range(0,10):
#for i in range(10):
#for i in range(0, 10, 3):
for i in range(10, 1, -3):
    print(i)

# List
#a=list() a=[] ,代表空list
#list.append(x) : 把x加到最後面
#list.insert(i, x) :把x加到i的位置上
#list.pop() : 刪除最後一個
#list.pop(i) : 把第(i)個掉
#list.remove(x) : 把第一個出現的x拿掉
#list.clear : 把list的資料刪光
#max(list): 找出list中的最大值
#min(list): 找出list中的最小值
#sum(list): 找出list中的數字加總
#list[start, end]: start和end 可以省略不寫
# start : default 0
# end : default len(list)
#list[:end] : 0 ~ end-1
#list[start] : start ~ len(list)-1
#list[:] : 0 ~ len(list)-1

a = ['Lynn', 0.87, 1234, True]
for i in range(0, len(a)):
    print(a[i])
for i in a:
    print(i)
print(a[:3])
print(a[2:])
print(a[:])

