#!/usr/bin/env python

#DATA type
# 1. Number
num1=3
num2=2
num3=num1/num2
print(type(num1))
print(type(num2))
print(type(num3))

# 2. String
str = 'abcdefasdsfa'
print('string len: ', len(str))
es_str=r'\t'
print('string len: ', len(es_str))
es2_str="""
a
ab
abc
"""
print('string len: ', len(es2_str))

# 3. Boolean
# in python , None==null
#python false值: False None [] {} "" set() () 0.0 
is_num_bigger_than_one  = 1>2
print(is_num_bigger_than_one) #False
x=None
print(x == None) #true

# 4. List
list_num = [1, 2, 3]
list = ['string', 1, [], list_num]
list_length = len(list_num)
num_sum=sum(list_num)
print(list_length)
print(num_sum)
x=range(10)
zero = x[0] 
nine = x[-1]
#x[0] = -1
print(x[:3])
print(x[3:])
print(x[1:5])
print(x[0:-1])
print(x[-1:-1])
print(1 in [1, 2, 3])
a=[1, 2, 3]
a.extend([4, 5, 6])
print(a[:])
b=a+[7, 8, 9]
print(b[:])
b.append(0)
print(b[:])

# 5. Tuple : 類似List，但宣告後不能修改。
my_list = [1, 2]
my_tuple = (1, 2)
my_list[1] = 3
try: 
    my_tuple[1] = 4
except TypeError:
    print('cannot modify a tuple')
x, y = 1, 2 
x, y = y, x
print(x, y)

# 6. Dictionary : 類似map，包含鍵值和key值
dict1 = {}
dict2 = dict()
grades = {'Mark': 70, 'Jack': 40}
print(grades['Mark'])
grades['KD'] = 100
print(len(grades), grades['KD'])
try:
    grade = grades['XD']
except KeyError:
    print('no grade for XD')
grades.get('XD',40)
print(grades.keys())
print(grades.values())
print(grades.items())
#defaultdict 
#一般作法
document=grades
word_counts={}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1
word_count = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

from collections import defaultdict
word_counts = defaultdict(int)
for word in document:
    word_counts[word] +=  1

# Set :栠合中不包括重複的元素值
s = set()
s.add(1)
s.add(2)
s.add(3)
print(len(s), 1 in s)

list_item = [1, 2, 3, 1, 2, 3]
set_item = set(list_item)
print(set_item)


