#50. Feb 19, 2021 - given 2 integer list (A, B), return True if A is subset of B or B is subset of A, return false ortherwise.
from typing import List
def isSubset(A: List[int], B: List[int]) -> bool:
    A = set(A)
    B = set(B)
    return A.issubset(B) or B.issubset(A)

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
print(isSubset(A , B))