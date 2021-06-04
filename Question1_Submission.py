def Pali(Str):
    j= len(Str)- 1
    for i in range(len(Str)//2):
        if Str[i] != Str[j]:
            return False
        j-= 1
        print(i)
    return True
if(Pali(input("Enter String: "))):
    print("It is a Palindrome")
else:
    print("It isn't a Palindrome")