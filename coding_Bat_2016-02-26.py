#! /usr/bin/env python3
# Warmup-1 > sleep_in 
"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in. 

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""

def sleep_in(weekday, vacation):
    if vacation or not weekday:
        return True 
    else:
        return False
        
"""
Other more concise variations did not work:
return if vacation or not weekday
if vacation or not weekday else return False

    if vacation or not weekday:
        return True
return False
"""

#! /usr/bin/env python3
# Warmup-1 > monkey_trouble 

"""

We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble. 

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""
def monkey_trouble(a_smile, b_smile):
    if (a_smile and b_smile) or (not a_smile and not b_smile):
        return True
    else:
        return False
"""More concise way, adapted after looking at GitHub answer to logic problem (see below)"""

def sleep_in(weekday, vacation):
    return vacation or not weekday

"""More concise way to do it (adapted from answer to Logic-1 > 01cigar_party.md on GitHub to jog my memory)"""

def monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or (not a_smile and not b_smile)

#! /usr/bin/env python3
# Warmup-1 > sum_double 
"""

Given two int values, return their sum. Unless the two values are the same, then return double their sum. 

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""

def sum_double(a, b):
    return (2 * (a + b)) if a == b else (a + b)

#! /usr/bin/env python3
# Warmup-1 > diff21 
"""
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21. 

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""

def diff2(n):
    return (2 * (abs(n - 21))) if n > 21 else (abs(n - 21))

#! /usr/bin/env python3
# Warmup-1 > parrot_trouble 
"""

We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble. 

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
"""

def parrot_trouble(talking, hour):
    return talking and not (7 > hour > 20)
"""
Tested hour variable in Python2:
>>> hour = 6
>>> return 7 > hour > 20
  File "<stdin>", line 1
SyntaxError: 'return' outside function
>>> 7 > hour > 20
False
>>> hour = 21
>>> 7 > hour > 20
False
>>> hour = 7
>>> 7 > hour > 20
False
>>> hour = 8
>>> 7 > hour > 20
False
>>> 
"""
def parrot_trouble(talking, hour):
    if talking:
        if hour < 7 or hour > 20:
            return True
        else:
            return False
            #Returned None if talking was false so added following
    else:
        return False

#! /usr/bin/env python3
# Warmup-1 > makes10
"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10. 

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
"""
def makes10(a, b):
    return (a + b == 10) or (a == 10) or (b == 10)

#! /usr/bin/env python3
# Warmup-1 > near_hundred 
"""

Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number. 

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""

def near_hundred(n):
    return (abs(n - 100) <= 10) or (abs(n - 200) <= 10)

#! /usr/bin/env python3
# Warmup-1 > pos_neg 
"""
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative. 

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""
def pos_neg(a, b, negative):
    if negative:
        return a < 0 > b
    else:
        return (a < 0 < b) or (a > 0 > b)

#! /usr/bin/env python3
# Warmup-1 > not_string 
"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged. 

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""
def not_string(str):
    if str.startswith('not'):
        return str
    else:
        return 'not {}'.format(str)

#! /usr/bin/env python3
# Warmup-1 > missing_char 

"""
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive). 

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""
def missing_char(str, n):
    return str.replace(str[n], '')

#! /usr/bin/env python3
# Warmup-1 > front_back 
"""
Given a string, return a new string where the first and last chars have been exchanged. 

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""
def front_back(str):
    stringFragment = str[1:(len(str)-2)]
    return '{}{}{}'.format(str[len(str) - 1], stringFragment, str[0])
"""The above appears to work in python3 but not in coding bat (python2)
Got index out of range error even though tested returning result of stringFragment and it worked ok
Documentation for Python 2.7.11 supports {}.format use
Update: Tested, following what's causing the index out of range error:
     return str[(len(str)-1)]
if you just do (len(str)-1) it returns the length minus 1
if you do str[0] in live python2 it works
so not sure why using it as index is causing out-of-range error
"""

#! /usr/bin/env python3
# Warmup-1 > front3

"""
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front. 

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""
#if word is 'to', word[0:3] returns 'to' with no errors
def front(str):
    return str[0:3] * 3