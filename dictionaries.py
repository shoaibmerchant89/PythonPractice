import operator

print('https://www.w3resource.com/python-exercises/dictionary/'.center(50,'-'))
print('-'.center(50,'-'))
print('Exercise 1'.center(50,'-'))
d = {'a':'10',
     'c':'13',
     'd':'1',
     'b':'22'
    }
l = (sorted(d.items(),key=operator.itemgetter(1)))
d = dict(l)
print(d)

print('-'.center(50,'-'))
print('Exercise 2'.center(50,'-'))
d1 = {0:10, 1:20}
d2 = {2:30, 3:40}
def add_key_to_dict(dict,key,value):
    dict[key] = value
    return dict
print(add_key_to_dict(d1,2,30))

print('-'.center(50,'-'))
print('Exercise 3'.center(50,'-'))
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)

print('-'.center(50,'-'))
print('Exercise 4'.center(50,'-'))
dic1 = {'a':'10','b':'20'}
def KeyInDict(key,dict):
    if key in dict:
        return 'Key found in dictionary'
    else:
        return 'Key not found in dictionary'

print(KeyInDict('a',dic1))

print('-'.center(50,'-'))
print('Exercise 5'.center(50,'-'))
dic1 = {
    'a':[0,1]
}
l = []
kl = []
vl = []
for k,v in dic1.items():
    kl.append(k)
    vl.append(v)
print(kl)
print(vl)