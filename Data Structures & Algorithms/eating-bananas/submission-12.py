class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right 

        while left <= right:
            mid = (left + right) // 2
            time = 0

            for i in range(len(piles)):
                time += (piles[i] + mid - 1) // mid

            if time <= h:
                res = mid
                right = mid - 1      
            else:
                left = mid + 1
        return res 