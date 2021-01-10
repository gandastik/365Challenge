#Jan 10, 2021 -sort the string input by their length
x = [str(x) for x in input().split()]
temp = dict()
for i in x:
    temp[len(i)] = i 

for i in sorted(temp.keys()):
    print("Length:", i, end="")
    print(" => " +temp[i])