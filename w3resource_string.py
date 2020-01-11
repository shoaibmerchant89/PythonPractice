print('='.center(100,'='))
print('https://www.w3resource.com/python-exercises/string/'.center(100,'-'))
print('='.center(100,'='))

print('\n'+'1'.center(100,'-'))
s = 'this is my string'
print(len(s))

print('\n'+'2'.center(100,'-'))
def char_frequency(string):
    d = {}
    for n in string:
        keys = d.keys()
        if n in keys:
            d[n] += 'y'
        else:
            d[n] = 'n'
    return d
print(char_frequency('google.com'))

print('\n'+'3'.center(100,'-'))
def first2last2(string):
    first2 = string[:2]
    last2 = string[-2:]
    if len(string) >= 2:
        return first2+last2
    else:
        return 'Empty String'
s = 'w'
print(first2last2(s))


print('\n'+'4'.center(100,'-'))
def replacefirst(str):
    newstr = str[0] + str[1:].replace(str[0], '$')
    return newstr
print(replacefirst('restart'))

print('\n'+'5'.center(100,'-'))
def first2swap(a,b):
    return b[:2] + a[2] + ' ' + a[:2] + b[2]
print(first2swap('abc','xyz'))


print('\n'+'6'.center(100,'-'))
def add_ing_ly(str):
    if len(str) >= 3 and str[-3:] != 'ing':
        return str + 'ing'
    if str[-3:] == 'ing':
        return str + 'ly'
    else:
        return str
print(add_ing_ly('ly'))


print('\n'+'7'.center(100,'-'))
'''
capture the starting index of word1 and starting index + length of word2 and save it into a variable.
str.replace that variable with the required value
'''
def first_appearence(str):
    snot = str.index('not')
    spoor = str.index('poor')

    rep = str[snot:(spoor+4)]
    if spoor > snot:
        str = str.replace(rep, 'good')
    return str
print(first_appearence('The lyrics is not that poor much'))

print('\n'+'8'.center(100,'-'))
'''
create an empty list word_len
run for loop against the word_list
for every item in the list - append thw word_len list with the length of the item that was iterated
use sort method to sort the list in the ascending order
return the last item in the list which should be the biggest number
'''
def biggestword(word_list):
    word_len = []
    for i in word_list:
        word_len.append((len(i)))
    word_len.sort()
    return word_len[-1]

l = ['apple','pineapple','pear','banana']
print(biggestword(l))

print('\n'+'9'.center(100,'-'))
'''
remove the character in a string at nth index
1st slice is up to nth
2nd slice is from n+1 to end
concatenate
'''
def removechar(n,str):
    first = str[:n]
    second = str[n+1:]
    return first+second
print(removechar(3,'Abercrombie'))

print('\n'+'10'.center(100,'-'))
'''
concatenate the last index + middle index + first index
'''
def firstlastexchanged(str):
    return str[-1] + str[1:-1] + str[0]
print(firstlastexchanged('shoaib'))


print('\n'+'11'.center(100,'-'))
'''
create empty string
run loop over the str for the range of length of str
if integer of range is a modulus of 2, then update result by adding the value of index i in s -->> s[i]
'''
def removeodd(s):
    result = ''
    for i in range(len(s)):
        if i % 2 == 0:
            result = result + s[i]
    return result
print(removeodd('shoaib'))


print('\n'+'12'.center(100,'-'))
'''
create empty string
run loop over the str for the range of length of str
if integer of range is a modulus of 2, then update result by adding the value of index i in s -->> s[i]
'''
def wordoccur(string):
    l = string.split()
    dict = {}
    for i in l:
#        keys = dict.keys()
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(wordoccur('the quick brown fox jumps over the lazy dog.'))

print('\n'+'13'.center(100,'-'))
'''
create an empty dictionary
take input from user
covert string into upper and lower case
print it in dictionary as values of d1 and d2
'''
def upperlower(s):
    d = {}
    #s = input()
    print('Expecting input here : {}'.format(s))
    su = s.upper()
    sl = s.lower()
    d.update({'d1':su,'d2':sl})
    return d
print(upperlower('hello'))

print('\n'+'14'.center(100,'-'))
'''
accept a comma separate sequence of words in a string
split string to list using comma
put list into a set to get unique items and run it with the sorted function to sort alphabetically
sorted list can also be reversed
'''
def uniquewords():
#    l = input()
    l = 'red,white,black,red,green,black'
    sl = sorted(set(l.split(',')), reverse=True)
    return sl
print(uniquewords())

print('\n'+'15'.center(100,'-'))
'''
pass two arguments in the function, one for each parameter
replace the parameter with format method
'''
def add_tags(a,b):
    return '<%s>%s</%s>' % (a,b,a)
print(add_tags('i','Python'))
print(add_tags('b','Python Tutorial'))

print('\n'+'16'.center(100,'-'))

print('\n'+'16'.center(100,'-'))
'''
create a function with one argument for string
capture the length of the string
divide the length by 2
use the result as an index
slice the string in two parts based on that index
concatenate first middle and last string
'''
def middle(a,b):
    i = int(len(a)/2)
    first = a[:i]
    last = a[i:]
    return first + b + last
print(middle('{{}}','PHP'))

print('\n'+'17'.center(100,'-'))
'''
slice a string at -2
multiply the slice with 4
'''
def fourcopies(s):
    return s[-2:]*4
print(fourcopies('Exercises'))

print('\n'+'18'.center(100,'-'))
'''
slice at :3 if s > 3
else return s
'''
def firstthree(s):
    return s[:3] if len(s) > 3 else s
print(firstthree('python'))

print('\n'+'19'.center(100,'-'))
'''
get part of string before /
split string at the match of /
return the string at index 0 of the split string
'''
def lastpart(s):
    return s.rsplit('/',1)[0]
print(lastpart('https://www.w3resource.com/python-exercises/string'))

print('\n'+'20'.center(100,'-'))
'''
len of s is modules of 4
reverse s
'''
def multipleof4(s):
    if len(s)%4 ==0:
        l = list(s)
        l.reverse()
        return ''.join(l)
print(multipleof4('fourfour'))

print('\n'+'21'.center(100,'-'))
'''
if 2 uppercase chars in first 4 chars
string = STRING
'''
def alluppercase(s):
    uppercount = 0
    for i in s[:4]:
        if i.isupper():
            uppercount += 1
    return s.upper() if uppercount >= 2 else s
#        else:
#            uppercount = 1
#    if uppercount >= 2 in s[:3]:
#        return s.upper()
print(alluppercase('PyThon'))

print('\n'+'22'.center(100,'-'))
'''
convert string to list
sort alphabetically(default for sorted)
join string back
'''
print(''.join(sorted(list('hello world!'))))

print('\n'+'23'.center(100,'-'))
'''
rstrip newline at the end of a string
'''
s = 'This is a new line\n'
print(s.rstrip())

print('\n'+'25'.center(100,'-'))
'''
string startswith specific chars within index range
'''
chars = 'new'
print('newlinestring'.startswith(chars,0,3))

print('\n'+'26'.center(100,'-'))
'''
align a long string using textwrap.fill library.method with width 50
'''
import textwrap
s = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
  '''
print(textwrap.fill(s,50))

print('\n'+'27'.center(100,'-'))
'''
use textwrap.dedent library.method to remove indentation from a piece of text
'''
print(textwrap.dedent(s))

print('\n'+'28'.center(100,'-'))
'''
use textwrap.indent library.method to add prefix to all lines in a string
'''
s1 = textwrap.dedent(s)
print(textwrap.indent(s,'> '))

print('\n'+'29'.center(100,'-'))
'''
use textwrap.indent library.method to indent the first line
'''
print(textwrap.fill(s1,initial_indent='',subsequent_indent=' '*4, width=80))

print('\n'+'38'.center(100,'-'))
'''
count occur of substring in a list of strings
'''
def occurstring(s,l):
    count = 0
    for i in l:
        if s in i:
            count += 1
        else:
            continue
    return count
l = ['This is the first string','This is the second string','and the third']
print(occurstring('string',l))

print('\n'+'39'.center(100,'-'))
'''
convert string to list
reverse list and re-convert back to string
'''
def reverse(s):
    return ''.join(reversed(s))
print(reverse('string'))

print('\n'+'41'.center(100,'-'))
'''
c = set of char to strip
.strip
'''
def stripchar(char,str):
    return ''.join(c for c in str if c not in char)
print(stripchar('aeiou','the quick brown fox jumps over the lazy dog'))

print('\n'+'42'.center(100,'-'))
'''
empty dictionary
for loop
for every char in for loop, add as keys in dictionary
of key found in string increment key value
if not then key = 1
'''
def charcount(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in sorted(d, key=d.get, reverse=True):
        if d[i] > 1:
            print('%s %d' % (i, d[i]))

print((charcount('thequickbrownfoxjumpsoverthelazydog')))

