#57. Feb 28, 2021 - given a list of integers, return the elements that has the integers is a square root.
from typing import List
def powerOfTwo(nums: List[int]) -> List[int]:
    ret = []
    for i in nums:
        if(i ** (1/2) == int(i ** (1/2))):
            ret.append(i)
    return ret

nums = [int(x) for x in input().split()]
print(powerOfTwo(nums))