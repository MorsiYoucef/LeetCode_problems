def isIsomorphic(self, s, t):
        mapp1={}
        mapp2={}

        for i in range(0,len(s),1):
            if ((s[i] in mapp1 and mapp1[s[i]] != t[i]) or \
                (t[i] in mapp2 and mapp2[t[i]] != s[i])):
                    return False
            mapp1[s[i]] = t[i]
            mapp2[t[i]] = s[i]
        return True
