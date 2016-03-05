#! /usr/bin/env python
# List-2 > count_evens 
"""
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1. 

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""
def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 ==0:
            count += 1
    return count

def count_evens(nums):
    evens = [1 for x in nums if x % 2 == 0]
    return sum(evens)
    
# Do it using reduce 
from functools import reduce

def count_evens(nums):
    return reduce(lambda acc, elem: acc+1 if elem % 2 == 0 else acc, nums, 0)

#! /usr/bin/env python
# List-2 > big_diff 
"""
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values. 

big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""
def big_diff(nums):
    return max(nums) - min(nums) 

#! /usr/bin/env python
# List-2 > centered_average
"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more. 

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""
def centered_average(nums):
    sorted_nums = sorted(nums)
    centered_nums = sorted_nums[1:-1]
    average_centered_nums = sum(centered_nums)/len(centered_nums)
    return average_centered_nums

#! /usr/bin/env python
# List-2 > sum13 

"""
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count. 

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""
def sum13(nums):
    unwanted_number = 13
    no_unwanteds = []
    if unwanted_number not in nums:
        return sum(nums)
    else:
        for i in xrange(len(nums)):
            if nums[i] != unwanted_number:
                if i == 0:
                    no_unwanteds.append(nums[i])
                else:
                    if nums[i-1] != unwanted_number:
                        no_unwanteds.append(nums[i])
    if no_unwanteds == []:
        return 0
    else:
        return sum(no_unwanteds)
#Sum of empty list returns 0 but making it explicit here
#Also probably could have done the above with a counter/accumulator

#! /usr/bin/env python
# List-2 > sum67 
"""Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers. 

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""
def sum67(nums):
    total = 0
    counting = True
    
    for x in nums:
        if x == 6:
            counting = False
        if x == 7 and not counting:
            counting = True
        elif counting:
            total += x
    return total

#! /usr/bin/env python
# List-2 > has22 
"""

Given an array of ints, return True if the array contains a 2 next to a 2 somewhere. 

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""
def has22(nums):
    found22 = False
    
    for x in xrange(len(nums)-1):
        if nums[x] == 2:
            if x == 0:
                if nums[x+1] == 2:
                    found22 = True
                    break
            else:
                if nums[x-1] == 2 or nums[x+1] == 2:
                    found22 = True
                    break

    return found22
# Couldn't just say "return if nums[x+1] == 2
# If first item was a 2 but wasn't followed by 2, would eval to False
#Then would return false and it wouldn't eval rest of array
#So added the variable
#But breaking if variable is true since that's all need to know
#i.e, if array contains 2 next to a 2 at any point in the array
