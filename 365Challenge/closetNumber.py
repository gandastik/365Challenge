#Jan 30, 2021 - find the closet number to the input.
n = int(input())
diff = 200000000000000
closetNum = 0
for i in range(8):
    x = int(input())
    if(abs(n - x) < diff):
        diff = abs(n - x)
        closetNum = x

print(closetNum)