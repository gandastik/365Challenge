#41. Feb 10, 2021 - find how many of prime number from 2 -> n (1 < n < 6000000)
def isPrime(n: int) -> bool:
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

def primeCount(n: int) -> int:
    count = 0
    for i in range(2,n):
        if(isPrime(i)):
            count += 1
    return count

n = int(input())
print(primeCount(n))