#36. Feb 5, 2021 - take n as input and take a list of numbers and the print out the stair case full with each element of the list
n = int(input())
nums = [int(x) for x in input().split()]
idx = len(nums) - 1

for i in range(n):
    for j in range(i+1):
        print(nums[idx], end='')
    print("")
    idx-=1