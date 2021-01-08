#Jan 8, 2021 - find number in list
n = int(input())
lst = [int(x) for x in input().split()]
target = int(input())
check = False
for item in lst:
    if(item == target):
        check = True
if(check):
    print("Yes")
else:
    print("No")