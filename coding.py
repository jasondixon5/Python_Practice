"""
a_smile
b_smile

if both a_smile and b_smile are True return True
if both a_smile and b_smile are False return True
else return False

if a==b:
	2 * (a+b)
else:
	(a+b)
	

def diff21(n):
    if n > 21:
		return 2 * abs((n - 21))
	else:
        return abs((n - 21))

if talking and hour < 7:
    return True
elif talking and hour >20:
    return True
elif:
    return False


100 - 93 = 7
100 - 90 = 10
100 - 89 = 11
100 - 10 = 90
100 - (-93) = 193
100 - 105 = -5
100 - 120 = -20


len(str)  #returns length of string
len(str) - 1 #returns length of string minus one
str[:] #returns string
str[0] #returns first letter
str[0:1] #returns first two letters

take everything up to index
take everything from one after index to end
	or take everything from end back to index
join the two?

take everything up to index 1 but not including it
str[0:1]
take everything from one after index 

def front_back(str):
    first_char = (str[0])
    last_char = (str[-1])
    


def front_back(str):
    if len(str) <= 1:
        return str
    else:
        str = str[-1] + str[1:-1] + str[0]
        return str
print(front_back(''))    
print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
"""
"""
def front3(str):
    
    return str[0:3] * 3
    
print(front3("Roosevelt"))
print(front3("Wa"))
print(front3("L"))
print(front3(" "))
print(front3(""))
"""
"""
name = "Bob"
print("Hello %s!") % (name)
"""
""""
def make_abba(a, b):
    print(a+b+b+a)

first = "Hi"
second = "Bye"

make_abba(first, second)
"""
""""
def make_tags(tag, word):
    print("<" + tag + ">" + word + "<" + "/" + tag + ">")
"""
"""
>>> 4 % 2
0
>>> 2 % 2
0
>>> 1 % 2
1
>>> 5 % 2
1
>>> 6 % 2
0
>>> 7 % 2
1
>>> 8 % 2
0
>>> 22 % 2
0
>>> 48 % 2
0
>>> 12453862 % 2
0
>>> string1 = "WooHoo"
>>> len(string1)
6
>>> len(string1) / 2
3
>>> string1[0:3]
'Woo'
>>> string2 = "HelloThere"
>>> len(string2)
10
>>> len(string2) / 2
5
>>> string2[0:5]
'Hello'
>>> string2[0:((len(string2)/2))]
'Hello'

string2
'HelloThere'
>>> string2[1]
'e'
>>> string2[1:]
'elloThere'
>>> string2[1:-1]
'elloTher'
>>> 

if len(a) >= len(b):
    b + a + b
else:
    a + b + a
    
"""