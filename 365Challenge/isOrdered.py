#56. Feb 25, 2021 - given a integers array, return true if it is in ascending or descending ordered.
from typing import List
def isOrdered(nums: List[int]) -> bool:
    rev = sorted(nums)
    rev.reverse()
    return nums == sorted(nums) or nums == rev

nums = [int(x) for x in input().split()]
print(isOrdered(nums))