#Jan 27, 2021 - find the character that are nexto & and return them.
def nextToAnd(string: str) -> str:
    count = 0
    if(len(string) != 5): return "Error"
    for i in string:
        if( i == '&') : count += 1
    if(count > 1 or count == 0): return "Error"
    a = string[string.index("&")-1]
    if(string.index("&") < len(string)-1):
        b = string[string.index("&")+1]
    else: return a
    b = string[string.index("&")+1]
    if(string.index("&") > 0):
        a = string[string.index("&")-1]
    else: return b
    if(a == b): return a
    else: return a + "," + b

string = str(input())
print(nextToAnd(string))