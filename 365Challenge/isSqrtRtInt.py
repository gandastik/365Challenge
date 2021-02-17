#48. Feb 17, 2021 - Given a List of integers, return the elements that has a integer square root.
from typing import List
def isSqrtRtint(nums: List[int]) -> List[int]:
    ret = []
    for i in nums:
        if(i ** (1/2) == int(i ** (1/2))):
            ret.append(i)
    ret.sort()
    return ret

nums = [int(x) for x in input().split()]
print(isSqrtRtint(nums))