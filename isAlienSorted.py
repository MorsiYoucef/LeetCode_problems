class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if(len(words) == 1 ):
            return True
        
        my_dict = {}
        for index,char in enumerate(order):
            my_dict[char] = index
        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if my_dict[w2[j]] <  my_dict[w1[j]]:
                        return False
                    break
        return True
        