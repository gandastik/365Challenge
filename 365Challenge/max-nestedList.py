#Jan 14, 2021 -find maximun sum of the elements in the nested list
from typing import List

def maximumWealth(accounts: List[List[int]]) -> int:
    ret = []
    for i in accounts:
        ret.append(sum(i))
    ret.sort()
    return ret[len(ret) - 1]

print(maximumWealth([[1,2,3,], [3,2,1]]))