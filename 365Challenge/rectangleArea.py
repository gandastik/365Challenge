#34. Feb 02, 2021 - find the area of the rectangle.
n = [float(x) for x in input().split()]
if(n[0] <= 0 and n[1] < 0):
    print("Invalid width and height")
elif(n[0] <= 0):
    print("Invalid width")
elif(n[1] <= 0):
    print("Invalid height")
else:
    print(n[0] * n[1])