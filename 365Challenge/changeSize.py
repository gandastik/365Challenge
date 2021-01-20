#Jan 20, 2021 -change a size of the string from upper case to lower and vice versa.
def changeSize(string: str) -> str:
    ret = ""
    for i in string:
        if(i.islower()):
            ret += i.upper()
        elif(i.isupper()):
            ret += i.lower()
    return ret

print(changeSize("ZANtaClaus"))