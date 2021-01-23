#Jan 23, 2021 - only take the input of 0 - 9 if the input is not in the condition
# print out how many of the input that go in
lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while(1):
    n = int(input())
    if(n < 0 or n >= 10):
        break
    lst[n] += 1

for i in range(10):
    print("%d = %d" % (i, lst[i]))