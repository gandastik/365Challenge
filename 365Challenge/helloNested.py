#Jan 29, 2021 - take a ,b as input return (0, 0) until (a, b) print new line every a times.
a = [int(x) for x in input().split()]
for i in range(a[0]+1):
    for j in range(a[1]+1):
        print("(%d, %d)" %(i, j), end='')
    print("")