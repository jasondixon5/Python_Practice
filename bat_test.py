#! /usr/bin/env python

from functools import reduce

def count_evens(nums):
    return reduce(lambda acc, elem: acc+1 if elem % 2 == 0 else acc, nums, 0)

print(count_evens([2, 1, 2]))


[7, 6, 8, 7, 9] #Expected: 16
[6, 8, 7, 8, 8] #Expected: 16
[6, 7]          #Expected: 0
