#46. Feb 15, 2021 - In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
# Return the element repeated N times.
from typing import List
def repeatedNTimes(A: List[int]) -> int:
    seen = set()
    for i in A:
        if( i not in seen):
            seen.add(i)
        else:
            return i 

A = [int(x) for x in input().split()]
print(repeatedNTimes(A))