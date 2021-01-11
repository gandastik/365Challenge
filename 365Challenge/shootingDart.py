#Jan 11, 2021 - finding how many arrow would it take to reach the given point
#assuming that there are 5 4 3 2 1 (in shooting dart)
n = int(input())
total = 0
if( n % 5 == 0):
    total += n / 5
else:
    total += (n // 5) + 1
print(int(total))