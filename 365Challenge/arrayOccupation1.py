#38. Feb 7, 2021 - make a reserves of the space of the array take N as the length of the array and
# K as the numbers of user's input, the user's input will be valid when it's value is between 1 and n (including 1 and n)
# output 1. how many user have the valid input 2. how many user that have the invalid input because of out of range
# 3. how many user have the invalid input because of the duplicate reservation of the space
# 4. the most index that being reserved (can be multiple)
n = int(input())
k = int(input())
arr = [int(x) for x in input().split()]
temp = [0 for i in range(k)]
completed = 0
outOfBound = 0
duplicated = 0
for i in range(len(arr)):
    if(arr[i] <= 0 or arr[i] > n):
        outOfBound += 1
    else:
        temp[arr[i]] += 1
for i in temp:
    if(i > 1):
        duplicated += i-1
completed = k - outOfBound - duplicated
print(completed)
print(outOfBound)
print(duplicated)
for i in range(len(temp)):
    if(temp[i] >= max(temp)):
        print("%d " %i, end="")