from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Step 1: Sort the array
        hand.sort()
        # Step 2: Count the occurrences of each card
        count = Counter(hand)

         # Step 3: Iterate over the sorted cards and try to form groups
        for card in hand:
             # If this card has already been used in a previous group, skip it
            if count[card] == 0:
                continue
            # Try to form a group starting from this card
            for i in range(groupSize):
                # If any card in the sequence [card, card + 1, ..., card + groupSize - 1] is missing, return False
                if count[card+i] == 0:
                    return False
                count[card+i] -= 1
        return True