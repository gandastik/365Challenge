#54. Feb 23, 2021 - Let's call an array arr a mountain if the following properties hold:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
from typing import List
def peakIndexInMountainArray(arr: List[int]) -> int:
    Max = max(arr)
    for i in range(len(arr)):
        if(arr[i] == Max):
            return i
        
arr = [int(x) for x in input().split()]
print(peakIndexInMountainArray(arr))