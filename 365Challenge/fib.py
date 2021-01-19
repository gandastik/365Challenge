#Jan 19, 2021 - write a function that calculate the nth term of fibonacci numbers.
def fib(n: int) -> int:
    lst = [0, 1]
    for i in range(2, n+1):
        lst.append(lst[len(lst)-2]+lst[len(lst)-1])
    return lst[n]

n = int(input())
print(fib(n))