#Jan 26, 2021 - simulating the accounting stuffs.
net = 0
income = 0
outcome = 0
income_c = 0
outcome_c = 0
while(1):
    n = int(input())
    if( n == 0 ) : break
    num = int(input())
    if( n == 1 ) :
        net += num
        income += num
        income_c += 1
    elif( n == 2 ) :
        net -= num
        outcome += num
        outcome_c += 1

print("%d %d" %(income_c, outcome_c))
print("%d %d %d" %(income, outcome, net))
