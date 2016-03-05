#! /usr/bin/env python
# List-1 > first_last6 
"""

Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more. 

first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
"""
def first_last6(nums):
    return nums[0] == 6 or nums[len(nums)-1] == 6

#! /usr/bin/env python
#List-1 > same_first_last
"""
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal. 

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
""" 
def same_first_last(nums):
    return len(nums) >=1 and nums[0] == nums[len(nums)-1]
#OR, using fact that last element in a list can be acc'd as index -1:
def same_first_last(nums):
    return len(nums) >=1 and nums[0] == nums[-1]

#! /usr/bin/env python
# List-1 > make_pi
"""
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}. 

make_pi() → [3, 1, 4]
"""
def make_pi():
    return [3, 1, 4]

#! /usr/bin/env python
# List-1 > common_end 

"""

Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more. 

common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True
"""
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

#! /usr/bin/env python
# List-1 > sum3 
"""
Given an array of ints length 3, return the sum of all the elements. 

sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
"""
def sum3(nums):
    sum(nums)
#or
def sum3(nums):
    y = 0
    for x in nums:
        y += x
    return y
#or
reduce(lambda acc, el: acc + el, l, 0)
#or
reduce(lambda acc, el: acc + el, l)
# in case of sum the acc value is ok as the first value in the list
#see below also

# to count number of 9's in the list (earlier problem)
reduce(lambda acc, el: acc+1 if el==9 else acc, l, 0)
#if you don't pass initial value (in this case 0), passes initial value of the accumulator (acc)  as first item in the list

#! /usr/bin/env python
# List-1 > rotate_left3 
"""
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}. 

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
"""
def rotate_left3(nums):
    first_popped = nums.pop(0)
    nums.append(first_popped)
    return nums
#also, using equivalent of .append per documentation website:
def rotate_left3(nums):
    nums[len(nums):] = [nums[0]]
    del nums[0]
    return nums

#! /usr/bin/env python
# List-1 > reverse3 
"""
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}. 

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
"""
def reverse3(nums):
    return nums[::-1]
# Note: If need to just change list in place can use list.reverse()

#! /usr/bin/env python
# List-1 > max_end3 
"""
Given an array of ints length 3, figure out which is larger between the first and last elements in the array, and set all the other elements to be that value. Return the changed array. 

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""
def max_end3(nums):
    max_value = max(nums[0], nums[-1])
    return [max_value for x in nums]

#! /usr/bin/env python
# List-1 > sum2 
"""
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0. 

sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2
"""
def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + nums[1]
#exception returned if index referenced is not in range
#if list is blank returns exception for list[0]
#so have to explicitly return 0 in that case
#*****correction below********* using slice which is easier
def sum2(nums):
    return sum(nums[0:2])
# A slice doesn't return an exception for a list of less than length 2
#A third option not using the built-in sum function is below

def sum2(nums):
    y = 0
    for x in nums[0:2]:
        y += x
    return y
    
# A fourth option using reduce

def sum2(nums):
    return reduce(lambda acc, el: acc+el, nums[0:2], 0)
#! /usr/bin/env python
# List-1 > middle_way 
"""
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements. 

middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
"""
def middle_way(a, b):
    return [a[1], b[1]]
#Now let's write it for an array of unknown length
def middle_way(a, b):
    if len(a) % 2 == 1:
        position = (int(round(len(a)/2.0)) - 1) #convert place of middle number to index position
        return [a[position], b[position]]
    else:
        position = len(a)/2 - 1
        return [a[position], b[position]]

#! /usr/bin/env python
# List-1 > make_ends 
"""
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more. 

make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]
"""
def make_ends(nums):
    return [nums[0], nums[-1]]

#! usr/bin/env python
# List-1 > has23
"""
Given an int array length 2, return True if it contains a 2 or a 3. 

has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
"""
def has23(nums):
    return 2 in nums or 3 in nums
