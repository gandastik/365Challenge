#Jan 25, 2021 - take 8 inputs calculate the sum of the even elements and odd elements,
#output what sum is bigger and their sum afterward.
lst = []
for i in range(8):
    n = int(input())
    lst.append(n)
even = 0
odd = 0
for i in lst:
    if( i % 2 == 0):
        even += i
    else :
        odd += i

if(odd > even): print("odd")
elif(even > odd) : print("even")
else : print("it's even")
print(even)
print(odd)
