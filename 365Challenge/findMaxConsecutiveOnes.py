#47. Feb 16, 2021 - Given a binary array, find the maximum number of consecutive 1s in this array.
from typing import List
def findMaxConsecutiveOnes(nums: List[int]) -> int:
    Max = -2000000000000
    count = 0
    for i in nums:
        if(i==0):
            count = 0
        else :
            count += 1
        if(count > Max):
            Max = count
    return Max

nums = [int(x) for x in input().split()]
print(findMaxConsecutiveOnes(nums))