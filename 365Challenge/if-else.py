# Jan 6, 2021 -if n is odd print Weird, n is even and inbetween 2 and 5 print Not Weird, 
# n is even and inbetween 5 and 20 print Weird, n is even and greater than 20 print Not Weird
n = int(input())
if(n % 2 != 0):
    print("Weird")
elif(n % 2 == 0 and n > 2 and n <= 5):
    print("Not Weird")
elif(n % 2 == 0 and n > 5 and n <= 20):
    print("Weird")
elif(n % 2 == 0 and n > 20):
    print("Not Weird")
