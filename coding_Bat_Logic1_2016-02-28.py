#! /usr/bin/env python
# Logic-1 > cigar_party 
"""
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise. 

cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
"""
"""
if cigars < 40 - False
if cigars >= 40 - check other conditions
if weekend and cigars >= 40 True
if not weekend and cigars <= 60 True
"""
def cigar_party(cigars, is_weekend):
    if cigars < 40:
        return False
    elif is_weekend or cigars <= 60:
        return True
    else:
        return False

#Following is the coding bat website's solution:
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return (cigars >= 40)
  else:
    return (cigars >= 40 and cigars <= 60)

#! usr/bin/env python
# Logic-1 > date_fashion 
"""
You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe). 

date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1
"""
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

#Slightly more readable
def date_fashion(you, date):
    no = 0
    maybe = 1
    yes = 2
    
    if you <= 2 or date <= 2:
        return no
    elif you >= 8 or date >= 8:
        return yes
    else:
        return maybe

#! /usr/bin/env python
# Logic-1 > squirrel_play 
"""
The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise. 

squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True
"""
def squirrel_play(temp, is_summer):
    if is_summer:
        return (temp >= 60 and temp <= 100)
    else:
        return (temp >= 60 and temp <= 90)

#! /usr/bin/env python
# Logic-1 > caught_speeding
"""
You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases. 

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
"""
def caught_speeding(speed, is_birthday):
    no_ticket = 0
    small_ticket = 1
    big_ticket = 2
    birthday_cushion = 5
    
    if is_birthday:
       speed -= birthday_cushion
    
    if speed <= 60:
        return no_ticket
    elif speed > 80:
        return big_ticket
    else:
        return small_ticket

#! /usr/bin/env python
# Logic-1 > sorta_sum 
"""
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20. 

sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
"""
def sorta_sum(a, b):
    if a + b in range(10, 20):
        return 20
    else:
        return a + b
# Alternate solution(from coding bat website)
def sorta_sum(a, b):
  sum = a + b
  if sum >= 10 and sum <= 19:
    return 20
  return sum

#! /usr/bin/env python
# Logic-1 > alarm_clock
"""

Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off". 

alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'
"""
# First pass at it
def alarm_clock(day, vacation):
    weekend = (0, 6)
    no_alarm = 'off'
    late_alarm = '10:00'
    early_alarm = '7:00'

    if vacation:
        if day in weekend:
            return no_alarm
        else:
            return late_alarm
    else:
        if day in weekend:
            return late_alarm
        else:
            return early_alarm

#Second pass at it with slightly more concise code
def alarm_clock(day, vacation):
    weekend = (0, 6)
    no_alarm = 'off'
    late_alarm = '10:00'
    early_alarm = '7:00'
    
    if vacation and day in weekend:
        return no_alarm
    elif vacation or day in weekend:
        return late_alarm
    else:
        return early_alarm

#! usr/bin/env python
# Logic-1 > love6 
"""
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number. 

love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True
"""
def love6(a, b):
    return (a == 6) or (b == 6) or (a + b == 6) or (abs(a - b) == 6)

#! /usr/bin/env python
# Logic-1 > in1to10 
"""
Given a number n, return True if n is in the range 1..10, inclusive. Unless "outsideMode" is True, in which case return True if the number is less or equal to 1, or greater or equal to 10. 

in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True
"""
def in1to10(n, outside_mode):
    return (outside_mode and (n <= 1 or n >= 10)) or (not outside_mode and (n in range(1, 11)))

#! /usr/bin/env python
# Logic-1 > near_ten 
"""
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod 

near_ten(12) → True
near_ten(17) → False
near_ten(19) → True
"""
def near_ten(num):
    # first write how to check if num a multiple of ten
    #   multiples of n can be divided by n w/out a remainder left over
    # then write if + or - 2 results in a multiple of 10
    #((num + 2) % 10 == 0) or ((num - 2) % 10 == 0)
    return num % 10 <= 2 or num % 10 >= 8
#Following is record of testing I did in command line
"""
>>> 118 + 2
120
>>> 120 % 10
0
>>> 122 + 2
124
>>> 124 % 10
4
>>> 122 - 2
120
>>> 120 % 10
0
>>> num = 12
>>> ((num + 2) % 10 == 0) or ((num - 2) % 10 == 0)
True
>>> num = 17
>>> ((num + 2) % 10 == 0) or ((num - 2) % 10 == 0)
False
>>> num = 19
>>> ((num + 2) % 10 == 0) or ((num - 2) % 10 == 0)
False
>>> 19 % 10
9
>>> 17 % 10
7
>>> 18 % 10
8
>>> 118 % 10
8
>>> 110 % 10
0
>>> 90 % 10
0
>>> 99 % 10
9
>>> 102 % 10
2
>>> 101 % 10
1
>>> 100 % 10
0
>>> num = 17
>>> num % 10 <= 2 or num % 10 >= 8
False
>>> num = 19
>>> num % 10 <= 2 or num % 10 >= 8
True
>>> num = 21
>>> num % 10 <= 2 or num % 10 >= 8
True
>>> num = 1021
>>> num % 10 <= 2 or num % 10 >= 8
True
>>> num = 25
>>> num % 10 <= 2 or num % 10 >= 8
False
>>> num = 99
>>> num % 10 <= 2 or num % 10 >= 8
True
>>> num = 102
>>> num % 10 <= 2 or num % 10 >= 8
True
"""
