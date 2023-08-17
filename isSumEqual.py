def isSumEqual(firstWord:str, secondWord:str, targetWord:str):
    char="abcdefghijklmnopqrstuvwxyz"
    listof1=[]
    listof2=[]
    listof3=[]

    for j in range(len(firstWord)):
        for i in range(len(char)):
            if firstWord[j]==char[i]:
                listof1.append(str(i))
    s=''.join(listof1)
    z=int(s)
    for j in range(len(secondWord)):
        for i in range(len(char)):
            if secondWord[j]==char[i]:
                listof2.append(str(i))
    a=''.join(listof2)
    y=int(a)
    for j in range(len(targetWord)):
        for i in range(len(char)):
            if targetWord[j]==char[i]:
                listof3.append(str(i))
    b=''.join(listof3)
    x=int(b)
    if z+y == x:
        return True
    else:
        return False

