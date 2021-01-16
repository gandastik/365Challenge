#Jan 16, 2021 -input two lists of integer determine wheter it's identical or not.
from typing import List
def isIdentical(a: List[int], b: List[int]) -> bool:
    if(len(a) != len(b)):
        return False
    else:
        a.sort()
        b.sort()
        for i in range(len(a)):
            if(a[i] != b[i]):
                return False
    return True

print(isIdentical([1,2,3,4,5], [5,3,1,2,4,20]))