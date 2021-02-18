#49. Feb 18, 2021 - write a function that takes in integers then check if every digits of the integers is in the ascending order.
def isIntAscending(n: int) -> bool:
    temp = n
    lst = []
    #extract the last digit of the number and append it in the list
    while(temp > 0):
        r = temp % 10
        lst.append(r)
        temp = temp // 10
    #check if lst[0] >= to every other elements in the list (contradiction to the idea of the problem)
    for i in range(1,len(lst)):
        if(lst[0] < lst[i]):
            return False
    return True

n = int(input())
print(isIntAscending(n))