#Jan 9, 2021 - find GCD of the 3 inputs
x, y, z = [int(x) for x in input().split()]
def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)
print("GCD: ", end="")
print(gcd(gcd(x, y), z))
