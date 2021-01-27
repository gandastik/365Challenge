#Jan 27, 2021 - compare the triplet between 2 list.
#If a[i] > b[i], then A is awarded 1 point.
#If a[i] < b[i], then B is awarded 1 point.
#If a[i] = b[i], then neither person receives a point.
#output num[2] = [(A-Points), (B-Points)]
from typing import List
def compareTriplet(a: List[int], b: List[int]) -> List[int]:
    ret = [0, 0]
    for i in range(len(a)):
        if(a[i] > b[i]) : ret[0] += 1
        elif(b[i] > a[i]) : ret[1] += 1
    return ret

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print(compareTriplet(a, b))