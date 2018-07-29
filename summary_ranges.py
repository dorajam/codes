"""
Given a sorted integer array without duplicates, return the summary of its ranges.
e.g.
for [0,1,2,4,5,7] -> ["0->2","4->5","7"]
for [0,2,3,4,6,8,9] -> ["0","2->4","6","8->9"]

July 2018, Dora Jambor.
Problem described on https://leetcode.com/problems/summary-ranges/description/
"""

def summary_ranges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if not nums:
        return nums
    res = []
    prev = nums[0]
    start = prev
    for e in nums[1:]:
        if start == prev:
            res.append(str(start))

        if prev + 1 == e:
            prev = e
            res[-1] = str(start) + '->' + str(prev)
        else:
            start = e
            prev = e

    if start == prev:
        res.append(str(start))
    return res


example1 = [0,1,2,4,5,7]
example2 = [0,2,3,4,6,8,9]

print summary_ranges(example1)
print summary_ranges(example2)
