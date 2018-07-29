"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
e.g.
for n=0  [1] -> invalid
for n=1  [1,1] -> 1
for n=2  [2,1,1] -> 2
for n=3, [1,2,3,1] -> 1

Notes:
1. You must not modify the array (assume the array is read only).
2. You must use only constant, O(1) extra space.
3. Your runtime complexity should be less than O(n2).
4. There is only one duplicate number in the array, but it could be repeated more than once.

July 2018, Dora Jambor
"""

def duplicate(arr):
    n = len(arr) - 1 

    seen = []
    for e in arr:
        if e not in seen:
            seen.append(e)
        else:
            return e
    print 'Seems like your array is unique'

print duplicate([1])
print duplicate([1,1])
print duplicate([2, 1,1])
print duplicate([3, 2, 3, 1])

