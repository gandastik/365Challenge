#35. Feb 4, 2021 - there's series that are (1−3+5−7+...+M )×(1−2+4−8+16−...−N) take input N and M.
#you can ignore the sign and print the output!
a = int(input())
b = int(input())
firstSeries = []
secondSeries = []
n = 0
while(True):
    firstSeries.append(int(((-1)**n) * (2*n+1)))
    if(firstSeries[n] == a or firstSeries[n] == a*(-1)):
        break
    n+=1
j = 0
while(True):
    secondSeries.append(int(((-1)**j) * (2**j)))
    if(secondSeries[j] == b or secondSeries[j] == b*(-1)):
        break
    j+=1

print(sum(secondSeries) * sum(firstSeries));