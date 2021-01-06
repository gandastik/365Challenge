# Jan 6, 2021 -input a set of string, check if there's a vowel.
string = str(input())
check = False
for i in string:
    if ( i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        check = True
if(check):
    print("Vowel")
else:
    print("No Vowel")