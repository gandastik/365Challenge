#39. Feb 8, 2021 - print horibargraph with the simple condition.
arr = []
i = 0
while(True):
    arr.append(int(input()))
    if(arr[i] <= 0):
        break
    i+=1

for i in arr:
    for j in range(1, i+1):
        if(j == i):
            print(i%10)
        elif(j % 5 == 0):
            print('X',end="")
        else:
            print("*",end="")