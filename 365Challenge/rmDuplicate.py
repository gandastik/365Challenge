#Jan 24, 2021 - remove consecutive duplicates of given list.
from typing import List
def removeDuplicate(nums: List[int]) -> List[int]:
    ret = []
    for i in range(len(nums)) :
        if(i == len(nums) - 1): ret.append(nums[i])
        elif(nums[i] != nums[i+1]):
            ret.append(nums[i])
    return ret

lst = [int(x) for x in input().split()]
print(removeDuplicate(lst))