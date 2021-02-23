#54. Feb 23, 2021 - given array of integers, return the list that only contain the prime number (return [0] if there's no prime in a given list).
from typing import List
def primeList(nums: List[int]) -> List[int]:
    def isPrime(n: int) -> bool:
        if(n <= 1): return False
        for i in range(2,n):
            if(n % i == 0):
                return False
        return True
    ret = []
    for i in nums:
        if(isPrime(i)):
            ret.append(i)
    if(len(ret) == 0):
        ret.append(0)
    return ret

nums = [int(x) for x in input().split()]
print(primeList(nums))