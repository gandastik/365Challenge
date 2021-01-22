#Jan 22, 2021 - binary search with the sorted list, return out the index if there is no element return -1.
from typing import List
def bSearch(lst: List[int], n: int, lo: int, hi: int) -> int:
    mid = int((lo+hi) / 2)
    if(lst[mid] == n):
        return mid
    elif(mid == lo) : return -1
    elif(lst[mid] > n):
        hi = mid
        return bSearch(lst, n, lo, hi)
    elif(lst[mid] < n):
        lo = mid
        return bSearch(lst, n, lo, hi)

def binarySearch(lst: List[int], n: int) -> int:
    return bSearch(lst, n, 0, len(lst))

lst = [int(x) for x in input().split()]
lst.sort()
n = int(input())
print(binarySearch(lst, n))