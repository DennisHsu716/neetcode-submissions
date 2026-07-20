class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)

        for card in sorted(hand):
            if count[card] == 0:
                continue
            
            for i in range(groupSize):
                cur = card + i

                if count[cur] == 0:
                    return False 
                count[cur] -= 1
        return True 