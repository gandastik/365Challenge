#Jan 15, 2021 - Write a function that return a shuffle array, 
# nums = [2,5,1,3,4,7]
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
from typing import List

def shuffle(nums: List[int], n: int) -> List[int]:
    l = int(len(nums) / 2)
    ret = []
    for i in range(l):
        ret.append(nums[i])
        ret.append(nums[i+l])
    return ret

print(shuffle([2,5,1,3,4,7], 3))