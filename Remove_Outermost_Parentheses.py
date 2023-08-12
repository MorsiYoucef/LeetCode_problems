def Outermost(s):
    ans = ""
    test = True
    j=0
    for i in range(len(s)):

            if s[i]=='(':
                j+=1
            elif s[i]==')':
                j-=1

            if j==1 and test ==True:
                test = False
                continue

            elif j==0 :
                test = True
                continue
            ans+=s[i]

    return ans
