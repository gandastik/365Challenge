#Jan 24, 2021 - insert a elements according to the list of indices
from typing import List
def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
    ret = []
    for i in range(len(nums)):
        ret.insert(index[i], nums[i])
    return ret
    
lst = [int(x) for x in input().split()]
index = [int(x) for x in input().split()]
print(createTargetArray(lst, index))