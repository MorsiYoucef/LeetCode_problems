def check(word1,word2):
    s=""
    z=""
    if len(word2)!=0:
      for i in range(len(word2)):
        s+=word2[i]
    else:
        s=''.join(word2)
    if len(word1)!=0:
      for i in range(len(word1)):
        z+=word1[i]
    else:
        z=''.join(word1)
    if s==z:
        return True
    else:
        return False

print(check(word1=["abce","d"],word2=["abcd"]))