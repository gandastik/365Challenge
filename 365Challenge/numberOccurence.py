#43. Feb 12, 2021 - find the occurence of given n in a list.
from typing import List
def numberOccurence(nums: List[int], n: int) -> List[int]:
    ret = []
    for i in range(len(nums)):
        if(nums[i] == n):
            ret.append(i+1)
    return ret

nums = [int(x) for x in input().split()]
n = int(input())
print(numberOccurence(nums, n))