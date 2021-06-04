def StrToInt(Arr1):
    Arr2= []
    for i in range(len(Arr1)):
        Arr2.append(int(Arr1[i]))
    return Arr2
def MaxWat(Arr):
    Max, l, h= 0, 0, 0
    for i in range(len(Arr)):
        for j in range(len(Arr)):
            l, h= (j- i), min(Arr[i], Arr[j])
            Max= max(Max, l * h)
    return Max
Arr= StrToInt(input("Enter: ").split(','))
print(MaxWat(Arr))