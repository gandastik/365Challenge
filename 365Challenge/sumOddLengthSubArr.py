#Feb 1, 2021 - Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
# A subarray is a contiguous subsequence of the array.
# Return the sum of all odd-length subarrays of arr.

from typing import List
def sumOddLengthSubarrays(arr: List[int]) -> int:
    n = int(len(arr) / 2)
    #taking a sum of every sub array that have length of array = 1
    ret = sum(arr)
    for i in range(n):
    #creating sub array by the size of (3, 5, 7, 9, ....) and slicing through the original array by array.length - (3, 5, 7, 9, ...) times 
    for j in range(len(arr) - 2*(i+1)):
            subArr = arr[j:2*(i+1)+1+j]
            ret += sum(subArr)
    return ret

n = [int(x) for x in input().split()]
print(sumOddLengthSubarrays(n))