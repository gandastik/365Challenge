#Jan 17, 2021 - find a max pairwise product of the given inputs.
from typing import List

def max_pairwise_product(lst: List) -> int:
    lst.sort()
    return lst[len(lst)-1]*lst[len(lst)-2]

n = int(input())
lst = [int(x) for x in input().split()]
print(max_pairwise_product(lst))