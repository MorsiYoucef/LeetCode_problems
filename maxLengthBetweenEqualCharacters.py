def maxLengthBetweenEqualCharacters(s):
        dic = {}
        for i in range (len(s)):
           dic[s[i]] = s.count(s[i])
        z=0
        x=0
        for y in dic.values():
            if y==2:
                z+=1
            if y==1 and z==1 :
                x+=1
            if 2 not in dic.values():
                return -1
        return x-1
              
print(maxLengthBetweenEqualCharacters(s="scayofdzca"))
        
    