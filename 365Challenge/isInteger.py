# Jan 7, 2020 -Check if the input is Integer or not
string = str(input())
check = True;
for i in string:
    if(i == '.'):
        check = False
if(check):
    print("Yes, It's Integer")
else :
    print("No, Itsn't Integer")