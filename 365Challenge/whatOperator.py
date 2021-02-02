#Day 33 :Feb 2, 2021 - find out what input that make A [] B = C (+ - * / % --> priority).
n = [int(x) for x in input().split()]
if(n[0] + n[1] == n[2]):
    print("+")
elif(n[0] - n[1] == n[2]):
    print("-")
elif(n[0] * n[1] == n[2]):
    print("*")
elif(n[0] // n[1] == n[2]):
    print("/")
elif(n[0] % n[1] == n[2]):
    print("%")