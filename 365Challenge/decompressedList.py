#Jan 23, 2021 - find the decompressed list consider each adjacent pair
#of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i>= 0).
from typing import List
def decompressedList(nums: List[int] ) -> List[int]:
    l = int(len(nums) / 2)
    ret = []
    for i in range(l):
        for j in range(nums[2*i]):
            ret.append(nums[2*i+1])
    return ret

n = [int(x) for x in input().split()]
print(decompressedList(n))