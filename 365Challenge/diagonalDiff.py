#Jan 26, 2021 - find the differece in the diagonal of the square matrix.
from typing import List 
def diagonalDifferent(nums) -> int:
    sumDiag = 0
    sum2Diag = 0
    j = 0
    k = len(nums) - 1
    for i in range(len(nums)):
        sumDiag += nums[i][j]
        sum2Diag += nums[i][k]
        k -= 1
        j += 1
    return abs(sumDiag - sum2Diag)

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
print(diagonalDifferent(arr), end='')