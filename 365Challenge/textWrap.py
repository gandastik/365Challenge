#Jan 22, 2021 - Wrap a string by input length.
def textWrap(string: str, num: int) -> str:
    l = int(len(string) / num)
    ret = ""
    for i in range(l+1):
        ret += string[i*num:i*num+num]
        ret += '\n'
    return ret

print(textWrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))