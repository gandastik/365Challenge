#Jan 17, 2021 - take a string as input and return out a string as the last two character of the input repeatedtly 4 times.
def insert_end(string: str) -> str:
    l = len(string)
    ret = string[l-2:]
    return ret * 4
print(insert_end("Exercises"))