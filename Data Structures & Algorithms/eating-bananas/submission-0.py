class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            time = 0 
            for i in range(len(piles)):
                time += (piles[i] + k - 1) // k

            if time <= h:
                res = k
                right = k - 1
            else:
                left = k + 1  
        return res   