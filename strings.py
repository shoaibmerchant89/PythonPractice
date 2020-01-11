import sys

class Students:
    pass

s1 = Students()
s2 = Students()

s1.first = 'heena'
s1.last = 'merchant'
s1.email = '@school.com'
s1.marks = '95'

s2.first = 'shoaib'
s2.last = 'heena'
s2.email = '@school.com'
s2.marks = '85'

print('My name is ' + s1.first + ' ' + s1.last + '. And my percentage in this semester is ' + s1.marks +'.')
print(s2.first)

def createfile(filename='FILE10.yaml'):
    '''
    Creates a yaml file and adds key-values within
    '''

    wf = open(filename, 'w')
    wf.write('==== ' + filename.strip('.yaml') + ' ====\n''color1: red\ncolor2: green\ncolor3: blue')
    wf.close()
    wf = open(filename).read()
    #wf = ''.join(wf)
    return print(wf)

def readfile(filename):
    '''
    reads a file
    '''
    rf = open(filename).read()
    return print(rf)

createfile('file4.yaml')
#print('\n')
readfile('file1.yaml')


def testx(x):
    if x:
        return print(True)
    else:
        return print()

testx('Spam')

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7]
def findinlist(list1, list2):
    if 1 in list1:
        print ('found 1')
    if 2 in list1:
        print('found 2')
    if 5 in list2:
        pass
    else:
        return ('not found')

print(findinlist(L1,L2))