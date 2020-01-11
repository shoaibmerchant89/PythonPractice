l1 =['apple1.yaml' , 'banana1.yaml' , 'mango1.yaml']
l2 = [4,5,6]

print('in list'.center(20, '-'))
for x in l1:
#    x = x.rstrip('.yaml')
    if '.yaml' in x:
        print(True)
    else:
        print(False)

print('append'.center(20, '-'))
import re
l1.append('orange.yaml')
if 'orange.yaml' in l1:
    print('orange found in list l1')
else:
    print('orange not found in list l1')

print(l1)

print('pop'.center(20, '-'))
l1.pop(-1)
if 'orange.yaml' in l1:
    print('orange found in list l1')
else:
    print('orange not found in list l1')
print(l1)

print('insert'.center(20,'-'))
if l1[0] == 'apple1.yaml':
    l1.insert(0,'lemon1.yaml')
    print(l1)
else:
    print('apple1.yaml not found')

print('for loop to update list'.center(40,'-'))
l3 = ['mango','banana','sweetlime','chickoo','apple','watermelon','muskmelon','grapes','kiwi','pomegranate']
l4 = ['apple','watermelon','sweetlime']
for item in l4:
    l3.remove(item)
print(l3)

print('append'.center(50, '-'))
l1 = ['apple1.yaml' , 'banana1.yaml' , 'mango1.yaml']
l2 = [4,5,6]
l3 = ['mango','banana','sweetlime','chickoo','apple','watermelon','muskmelon','grapes','kiwi','pomegranate']
l4 = ['apple','watermelon','sweetlime']


l2.insert(1, 10)
print(l2)
l2.pop(1)
print(l2)
l2.remove(4)
print(l2)
l2.reverse()
print(l2)
l3.sort()
print(l3)

print('\n' + 'SETS'.center(100,'=') + '\n')

fruits = {'apple', 'mango'}
for x in fruits:
    print(x)
myfruits = {'mango'}

fruits.update(["pineapple", "banana"])
print(fruits.difference_update(myfruits))

fruits.pop()
print(fruits)

l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']

print('\n' + 'DICTIONARY'.center(20, '=') + '\n')
dict1 = {'make': 'dell', 'model':'inspiron', 'series':'5000'}
print('two ways to get values form a dictionary'.center(50,'-') + '\n')
print('1st method = ' + dict1['make'])
print('2nd method = ' + dict1.get('model') + '\n')
print('change value of key \'model\' from dell to HP'.center(50, '-') + '\n')
dict1['make'] = 'HP'
print(dict1['make'] + '\n')
print('loop through a dictionary'.center(50,'-'))
def dictloop1(dictionary):
    for x in dictionary:
        k = x
        v = dictionary[x]
        print(k + ' : ' + v)
    print('func dictloop1')
def dictloop2(dictionary):
    for x, y in dictionary.items():
        print(x + ' : ' + y)
    print('func dictloop2')

dictloop1(dict1)
print('-------')
dictloop2(dict1)
print('\n')
print('check if key exists in dictionary'.center(50, '-'))
dict2 = {'make':'Acer','model':'aspire','series':'5000'}
def indict(dictionary1,dictionary2):
    for x in dictionary1:
        y = dictionary1[x]
    if y in dictionary2[x]:
        print(True)
    else:
        print(False)
    print('\n')
indict(dict1,dict2)

print('add items to dictionary'.center(50,'-') + '\n')

def additems(dictionary,key,value):
    dictionary[key] = value
    print(dictionary)
#
#dict1['ram'] = '4gb'
#dict1['cpu'] = '3ghz'
#print(dict1)
#
#dict2['ram'] = '8gb'
#dict2['cpu'] = '2.4ghz'
#print(dict2)
#print('\n')
#
additems(dict1,'ram','4gb')
print('remove items from dictionary'.center(50,'-') + '\n')
del dict1['make']
print(dict1)
print('create nested dictionaries'.center(50,'-'))
myfamily = {
    'elders':{
        'elder1':{
            'name':'shahnawaz',
            'age':'58'
        },
        'elder2':{
            'name':'naazleen',
            'age':'52'
        }
    },
    'millenials':{
        'mil1':{
            'name':'shoaib',
            'age':'29'
        },
        'mil2':{
            'name':'heena',
            'age':'30'
        }
    },
    'children':{
        'child1':{
            'name':'sarah',
            'age':'0.10'
        }
    }
}
print(myfamily)
import json
myjson = json.dumps(myfamily, indent=4)
print(myjson)
mydict = json.loads(myjson)
print(mydict['elders']['elder1']['name'])
print(dict1.values())
print(str(dict2.values()) + '\n')

print('IF and ELSE'.center(50,'-'))
a = 10
b = 11


print('nested if, method 1 - print when multiple values are true'.center(70,'-'))
if a >= b:
    print('a > b')
    if a == b:
        print('and \na = b')
    else:
        print('but \na != b')
else:
    print('b > a')

print('nested if, method 2- print when multiple values are true'.center(70,'-'))
if a > b and a == b:
    print('a > b\nand\na = b')
elif a > b and a != b:
    print('a > b\nbut a != b')
else:
    print('b > a')

print('WHILE LOOP'.center(50,'-') + '\n')
i = 0
while i <= 6:
    i += 1
    if i == 3 or i == 2:
        continue
    print(i)
else:
    print('i is no longer less than 6')

m = 11
while m != 0:
    m = m-1
    if m % 2 !=0: continue
    print(m, end=' ')

print('\n' + 'FOR'.center(50,'-') + '\n')

s = 'shoaib'
for item in myfamily.items():
    print(item)

for each in s:
    if each == 'xx':
        break
    for x in range(10):
        print(each)

def myfunc(kids, parents):
    print('The youngest child is ' + kids + parents)

myfunc('Emil','Tobias')

print('CLASSES'.center(50,'-'))
class myclass:
    x = myfamily
    y = myfruits
p1 = myclass()
print(p1.x['elders']['elder1']['name'])
print(type(p1.y))
print('-'.center(50,'-'))
class class1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myname(abc):
        print('my name is ' + abc.name)
p1 = class1('John',59)
print(p1.name)
del p1.age
p1.myname()

#print(p1.age)
def func10(name,age):
    return print(name + '\n' + age)

func10('John','58')

list1 = [1,2,3,4,5]
def sum_list(l):
    return sum(l)
print(sum_list(list1))


print('----------------------------')
a = (17, 28, 30)
b = (99, 16, 8)
def compareTriplets(a, b):
    acount = 0
    bcount = 0
    for x in range(len(a)):
        if a[x] > b[x]:
            acount += 1
        elif b[x] > a[x]:
            bcount += 1
    return [acount, bcount]
print(compareTriplets(a,b))