#Day 33 :Feb 2, 2021 - Given an array of integers, calculate the ratios of its elements
#that are positive, negative, and zero. print the decimal value of each fraction on a new line with 6 places after the decimal.
def plusMinus(arr):
    pos = 0
    zero = 0
    neg = 0
    for i in arr:
        if(i > 0):
            pos += 1
        elif(i < 0):
            neg += 1
        elif(i == 0):
            zero += 1
    print("%.6f" % (pos/float(len(arr))))
    print("%.6f" % (neg/float(len(arr))))
    print("%.6f" % (zero/float(len(arr))))

plusMinus([1,1,0,-1,-1])