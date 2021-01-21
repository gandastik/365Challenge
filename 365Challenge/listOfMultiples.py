#Jan 21, 2021 - Create a functions that takes two numbers as arguments
#(num, length) and returns a list of multiples of num until the list length reaches length.
from typing import List

def lstOfMultiples(num: int, length: int) -> List[int]:
    ret = []
    for i in range(1, length+1):
        ret.append(num*i)
    return ret

x , y = [int(x) for x in input().split()]
print(lstOfMultiples(x, y))