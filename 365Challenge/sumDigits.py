#52. Feb 21, 2021 - given start and end, return list that have element between start to end(not inclusive) 
# that has the sum of every digits equal to 10
from typing import List
def sumDigitstoTen(start: int, end: int) -> List[int]:
    ret = []
    for i in range(start,end):
        temp = i
        totalSum = 0
        while(temp > 0):
            totalSum += temp % 10
            temp = temp // 10
        if(totalSum == 10):
            ret.append(i)
    return ret

start = int(input())
end = int(input())
print(sumDigitstoTen(start, end))