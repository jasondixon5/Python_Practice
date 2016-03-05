#! /usr/bin/env python
# String-2 > double_char 
"""
Given a string, return a string where for every char in the original, there are two chars. 

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
"""
def double_char(str):
    new_str = ''
    for l in str:
        new_str += 2 * l
    return new_str
#Solution from coding bat website:
def double_char(str):
  result = ""
  for i in range(len(str)):
    result += str[i] + str[i]
  return result

#! /usr/bin/env python
# String-2 > count_hi 
"""
Return the number of times that the string "hi" appears anywhere in the given string. 

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""
def count_hi(str):
    count = 0
    for l in xrange(len(str)-1):
        if str[l] == 'h' and str[l+1] == 'i':
            count += 1
    return count

#workable alternative
def count_hi(str):
    count = (1 for l in xrange(len(str)-1) if str[l] == 'h' and str[l+1] == 'i')
    #yields generator object
    #found below examples to extract result but not sure why works:
    total = 0
    for i in count:
        total += i
    return total

#solution from coding bat website:
#I like this because it uses slice instead of two separate comparisons
def count_hi(str):
  sum = 0
  ## Loop to length-1 and access index i and i+1
  ## in the loop.
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      sum = sum + 1
  return sum

#! /usr/bin/env python
#  String-2 > cat_dog
"""
Return True if the string "cat" and "dog" appear the same number of times in the given string. 

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""
def cat_dog(str):
    cat_total = 0
    dog_total = 0
    for i in range(len(str)-2):
        if str[i:i+3] ==  'cat':
            cat_total += 1
        elif str[i:i+3] == 'dog':
            dog_total += 1
    return cat_total == dog_total

#! usr/bin/env python
# String-2 > count_code 
"""
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count. 

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""
def count_code(str):
    count = 0
    for i in xrange(len(str)-3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            count += 1
    return count
#Now same problem but with better condition checking
#Problem said we'll accept any letter for third character so going to make sure it's actually a letter (upper- or lowercase)

def count_code(str):
    count = 0
    upper_alpha = [chr(i) for i in xrange(65, 91)]
    lower_alpha = [chr(i) for i in xrange(97, 123)]
    
    for i in xrange(len(str)-3):
        if str[i:i+2] == 'co' and (str[i+2] in upper_alpha or str[i+2] in lower_alpha) and str[i+3] == 'e':
            count += 1
    return count

#! /usr/bin/env python
# String-2 > end_other
"""
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string. 

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""
def end_other(a, b):
    a_lower = a.lower()
    b_lower = b.lower()
    return a_lower == b_lower[-(len(a)):] or b_lower == a_lower[-(len(b)):]

#! /usr/bin/env python
# String-2 > xyz_there 
"""
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not. 

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
"""
def xyz_there(str):
    test_string = 'xyz'
    if len(str) < 4:
        return str == test_string
    else:
        return (test_string in str) and (str[str.index(test_string) - 1] != '.')
#The above works in that it finds an appearance of xyz but it's not complete.
#Although the problem is worded badly, testing it on the website shows they are looking for **no** appearances of xyz to be preceded by a dot/period
#So update is below:
#***Update to update** Jason pointed out that 'xyz.' would not evaluate correctly
#So updated below to make sure that str[i-1] does not evaluate to str[-1]
#str[-1] would evaluate to last item in string, which if it was . would cause an incorrect False result

def xyz_there(str):
    test_string = 'xyz'
    test_string_found = False
    if len(str) < 4:
        return str == test_string
    else:
        for i in xrange(len(str)):
            if str[i:i+3] == test_string and (i == 0 or str[i-1] != '.'):
                test_string_found = True
    return test_string_found

