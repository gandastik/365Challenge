#55. Feb 24, 2021 - given two string ,return the special characters of the string that have the most of it.
from typing import List
def specialChar(a: str, b: str) -> List[str]:
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter_a = 0
    counter_b = 0
    lst_a = []
    lst_b = []
    for i in a:
        if(i not in alphabet):
            counter_a += 1
            lst_a.append(i)
    for i in b:
        if(i not in alphabet):
            counter_b += 1
            lst_b.append(i)
    if(counter_a >= counter_b):
        return lst_a
    return lst_b

a = str(input())
b = str(input())
print(specialChar(a, b))