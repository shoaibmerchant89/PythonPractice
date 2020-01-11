def createnewfile(file):
    with open(file,mode='w') as f:
        f.write('This is a newly created file using the function createnewfile()')

def clearfilecontent(file):
    with open(file,mode='w') as f:
        f.write('')

def addnewline(file,car,number):
    with open(file,mode='r+') as f:
        for n in range(0, number):
            if len(car) > n:
                f.write(str(n) + '\tA new line has been added for = ' + car[n] + '\n')
            else:
                break
        else:
            f.write('END of LINE')

def printfile(file):
    with open(file,mode='r') as f:
        print(f.read())

carlist = ['i10','grandi10','i10nios','xcent','venue','verna','creta']

clearfilecontent('abc.txt')
createnewfile('abc.txt')
addnewline('abc.txt',carlist,8)
printfile('abc.txt')

def findinstring(word,string):
    return word in string
    return word not in string


string = 'lazy fox jumped over the river'
print(findinstring('foxy',string))

def piglatin(word):
    if word.startswith(('a','e','i','o','u')):
        pig_word = str(word) + 'ay'
        return pig_word
    else:
        word = list(word)
        w1 = word[0]
        word = ''.join(word[1:])
        newword = word + w1 + 'ay'
        return newword

print(piglatin('apple'))
print(piglatin('word'))

def pig_latin(word):
    firstletter = word[0]

    if firstletter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + firstletter + 'ay'
    return pig_word

print(pig_latin('apple'))
print(pig_latin('word'))

print('WARM UP PROBLEMS'.center(50,'-'))
print('lesser_of_two_evens'.center(50,'-'))
def lesser_of_two_evens(n1,n2):
    if n1 % 2 == 0 and n2 % 2 == 0:
        return min(n1,n2)
    else:
        return max(n1,n2)
print(lesser_of_two_evens(2,4))


print('animal_crackers'.center(50,'-'))
def animal_crackers(s):
    l = s.split(' ')
    l0_first = l[0][0]
    l1_first = l[1][0]
#    l0_first = l0_first[0]
#    l1_first = l1_first[0]
    return l0_first == l1_first
print(animal_crackers('Levelheaded Llama'))

print('makes_twenty'.center(50,'-'))
def makes_twenty(i1,i2):
    if i1 + i2 == 20 or i1==20 or i2==20:
        return True
    else:
        return False
print(makes_twenty(20,2))

print('LEVEL 1 PROBLEMS'.center(50,'-'))
print('old_macdonald'.center(50,'-'))
def old_macdonald(name):
    n1 = name[0:3].capitalize()
    n2 = name[3:].capitalize()
    return n1 + n2
print(old_macdonald('macdonald'))

print('master_yoda'.center(50,'-'))
def master_yoda(s):
    s = s.split(' ')
    s.reverse()
    s1 = ' '.join(s)
    return s1
print(master_yoda('We are ready'))

print('almost_there'.center(50,'-'))
def almost_there(n):
    return n in range(90,110) or n in range(190,210)
print(almost_there(209))


print('LEVEL 2 PROBLEMS'.center(50,'-'))
print('has_33'.center(50,'-'))
def has_33(l):
    for i in range(len(l) -1):
        if l[i] == l[i+1]:
            return True
    return False

print(has_33([1,3,3]))

print('paper_doll'.center(50,'-'))
def paper_doll(string):
    l = []
    for x in string:
        x3 = x*3
        l.append(x3)
    s3 = ''.join(l)
    return s3
print(paper_doll('Mississippi'))

print('blackjack'.center(50,'-'))
def blackjack(n1,n2,n3):
    n = n1+n2+n3
    if n <= 21:
        return n
    elif n1==11 or n2==11 or n3==11 and n>=21:
        return n-10
    else:
        return 'BUST'
print(blackjack(9,9,11))

print('summer_69'.center(50,'-'))
def summer_69(array):
    total = 0
    add = True
    for num in array:
        while add==True:
            if num !=6:
                total += num
                break
            else:
                add = False
        while add==False:
            if num !=9:
                break
            else:
                add = True
                break
    return total
print(summer_69([2,1,6,9,11]))

print('spy_game'.center(50,'-'))
def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            nums.pop(0)
    return len(code) == 1
print(spy_game([0,0,7,1,1,2]))


print('LAMBDA EXPRESSIONS'.center(50,'-'))
def square(num):
    return num**2
list1 = [1,2,3,4,5]
print(list(map(square,list1)))
print(list(map(lambda num:num**2,list1)))

