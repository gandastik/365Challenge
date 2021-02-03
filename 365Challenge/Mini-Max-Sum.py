#34. Feb 3, 2021 - given five positive integers, find the minimum and maximum values that
#can be calculated by summing exactly four of the five integers.
from typing import List
def miniMaxSum(arr: List[int]):
    arr.sort()
    Min = sum(arr[:len(arr)-1])
    Max = sum(arr[1:])
    print("%d %d" % (Min, Max))

arr = [int(x) for x in input().split()]
miniMaxSum(arr)