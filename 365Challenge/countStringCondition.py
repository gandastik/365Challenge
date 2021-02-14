#45. Feb 14, 2021 - take string as an input.
#return 1 when upper case alphabet is presence more
#return 2 when lower case alphabet is presence more
#return 3 when number presence more
#return 4 when two or more type have the greatest amount of presence
def countStringCondition(s: str) -> int:
    lower = 0
    upper = 0 
    number = 0
    for i in s:
        if(i.islower()):
            lower += 1
        elif(i.isupper()):
            upper += 1
        else:
            number +=1
    if(upper > lower and upper > number):
        return 1
    elif(lower > upper and lower > number):
        return 2
    elif(number > upper and number > lower):
        return 3
    else:
        return 4

s = str(input())
print(countStringCondition(s))