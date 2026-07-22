class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)

        for card in sorted(hand):
            if count[card] == 0:
                continue 
            
            for i in range(groupSize):
                curr = card + i

                if count[curr] == 0:
                    return False 
                
                count[curr] -= 1
        return True