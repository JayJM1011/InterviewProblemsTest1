 def Occ(Sub):
    String1= ""
    for index in range(len(String1)- 2):
        if Sub[0] == String1[index] and Sub[1] == String1[index+ 1] and Sub[2] == String1[index+ 2]:
            return index
    return 0

def LetterToNum(Let):
    if Let == 'A':
        return 0
    if Let == 'B':
        return 1
    if Let == 'C':
        return 2
    if Let == 'D':
        return 3
    if Let == 'E':
        return 4
    if Let == 'F':
        return 5
    if Let == 'G':
        return 6
    if Let == 'H':
        return 7
    if Let == 'I':
        return 8
    if Let == 'J':
        return 9
    if Let == 'K':
        return 10
    if Let == 'L':
        return 11
    if Let == 'M':
        return 12
    if Let == 'N':
        return 13
    if Let == 'O':
        return 14
    if Let == 'P':
        return 15
    if Let == 'Q':
        return 16
    if Let == 'R':
        return 17
    if Let == 'S':
        return 18
    if Let == 'T':
        return 19
    if Let == 'U':
         return 20
    if Let == 'V':
        return 21
    if Let == 'W':
        return 22
    if Let == 'X':
        return 23
    if Let == 'Y':
        return 24
    if Let == 'Z':
        return 25

Point, Key= 0, ""
SubStr1, SubStr2, SubStr3= "BWC", "PKW", "QKA"

String2= ""

Point= Occ(SubStr1)
Key+= String2[Point]

Point= Occ(SubStr2)
Key+= String2[Point]

Point= Occ(SubStr3)
Key+= String2[Point]

print("Key:", Key)

Lets= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
CipherStr= ""
for i in range(3):
    CipherStr+= Lets[(LetterToNum(Key[i]) + LetterToNum(SubStr1[i])) % 25]
print("SubString 1:", CipherStr)

CipherStr= ""
for i in range(3):
    CipherStr+= Lets[(LetterToNum(Key[i]) + LetterToNum(SubStr2[i])) % 25]
print("SubString 2:", CipherStr)

CipherStr= ""
for i in range(3):
    CipherStr+= Lets[(LetterToNum(Key[i]) + LetterToNum(SubStr3[i])) % 25]
print("SubString 3:", CipherStr)
