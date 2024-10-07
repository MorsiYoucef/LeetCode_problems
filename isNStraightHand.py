from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count = Counter(hand)


        for card in hand:
            if count[card] == 0:
                continue
            
            for i in range(groupSize):
                if count[card+i] == 0:
                    return False
                count[card+i] -= 1
        return True