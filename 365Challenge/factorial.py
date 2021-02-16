#47. Feb 16, 2021 - Given a list of integer, return the list with each of the elements being the factorial products of their own elements.
from typing import List
def factorialList(nums: List[int]) -> List[int]:
    def factorial(n: int) -> int:
        if(n == 1):
            return n
        return n*factorial(n-1)
    ret = []
    for i in nums:
        ret.append(factorial(i))
    return ret

nums = [int(x) for x in input().split()]
print(factorialList(nums))
