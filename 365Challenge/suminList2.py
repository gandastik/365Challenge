#Jan 12, 2021 -check if every element in the list is less than the sum of the rest of the elements
lst = [int(x) for x in input().split()]
check = True
for i in lst:
    if ( i > sum(lst)-i):
        check = False
print(check)