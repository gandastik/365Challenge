#Jan 15, 2021 - find out if the input list is empty or not
from typing import List

def isEmpty(lst: List[int]) -> bool:
    return True if len(lst) == 0 else False

print(isEmpty([]))