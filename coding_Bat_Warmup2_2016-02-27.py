#! /usr/bin/env python
# Warmup-2 > string_times
"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string. 

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""
def string_times(str, n):
    return str * n
    
#! /usr/bin/env python
# Warmup-2 > front_times 
"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front; 

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""
def front_times(str, n):
    return str[0:3] * n

#! /usr/bin/env python
# Warmup-2 > string_bits
"""

Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo". 

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""
def string_bits(str):
    return str[::2]

#! /usr/bin/env python
# Warmup-2 > string_splosion 
"""
Given a non-empty string like "Code" return a string like "CCoCodCode". 

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""
# Need to iterate through string
#   Need to keep track of position (counter for index?)
# Need to slice string at progressive positions
# Need to join slice with earlier slice
# Need to iterate number of times equalling length of string
# But need to expand slice each time

def string_splosion(str):
    new_list = []
    for l in xrange(len(str)+1):
        new_list.append(str[0:l])
    new_string = ''.join(new_list)
    return new_string

#! /usr/bin/env python
# Warmup-2 > last2 
"""

Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring). 

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""
def last2(str):
    count = 0
    test_string = str[len(str)-2:]
    for i in range(0, len(str)-2):
        if str[i] + str[i+1] == test_string:
            count += 1
    return count

#! /usr/bin/env python
# Warmup-2 > array_count9
"""Given an array of ints, return the number of 9's in the array. 

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""
#Two ways of doing this. 
#First way:
def array_count9(nums):
    count = 0
    for x in nums:
        if x == 9:
            count += 1
    return(count)
#Second way using list comprehension

def array_count9(nums):
    return len([x for x in nums if x == 9])

#Uses generator comprehension
#Generator comprehension returns a generator object
#Generator object returns items one at a time but doesn't hold all items in memory at once
#So can clal .next() to get next item in generator
# "For" loop under the hood calls .next() for each item in iterable

def array_count9(nums):
    return sum(1 for x in nums if x == 9)
    

#! /usr/bin/env python
# Warmup-2 > array_front9 
"""

Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4. 

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""
def array_front9(nums):
    return 9 in nums[0:3]
#Doesn't return an error if list is less than 4 elements long
#Can be more conservative in error-checking
    if len(nums) <= 4:
        return 9 in nums[0:len(nums)]
    else:
        return 9 in nums[0:4]

#! /usr/bin/env python
#Warmup-2 > array123
"""
Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere. 

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""
def array123(nums):
    for x in xrange(len(nums)):
        if nums[x:x+3] == [1, 2, 3]:
            return True
    return False

#! /usr/bin/env python
# Warmup-2 > string_match
"""

Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings. 

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""
def string_match(a, b):
    count = 0
    test_length = min(len(a), len(b))
    
    for x in xrange(test_length-1):
        if a[x:x+2] == b[x:x+2]:
            count += 1
    return count
    
