# Jan 8, 2021 -check if the square root of the input if Integer or not.
num = float(input())
if int(num**(1/2)) == num**(1/2):
    print("Yes, It's Integer")
else:
    print("No, It's not Integer")