#Jan 19, 2021 - write a function that take interger as parameter and return the sum between 1 to n (time complexity O(1)).
def sumUp(n: int) -> int:
    return n/2 * (1 + n)

n = int(input())
print(sumUp(n))