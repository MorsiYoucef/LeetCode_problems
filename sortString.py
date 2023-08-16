def sortString( s):
    result=[]
    char="abcdefghijklmnopqrstuvwxyz"
    while s:
        for c in char:
            if c in s:
                result.append(c)
                s = s.replace(c,'',1) #Replace the first occurrence of the letter 'c' by ''
            else:
                char = char.replace(c,'')
        char=char[::-1] #to reverce char
    return ''.join(result) #result=['a','b','c'] -> abc
print(sortString("aaabbbccc"))