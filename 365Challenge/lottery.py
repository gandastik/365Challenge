#40. Feb 9, 2021 - find the last 3 number of the lottery picked in the lottery bought list
lotteryBought = [str(x) for x in input().split()]
lotteryPicked = [str(y) for y in input().split()]
count = 0
for i in lotteryPicked:
    for j in lotteryBought:
        temp = j[len(j)-3:]
        if(temp == i):
            count += 1

print(count)