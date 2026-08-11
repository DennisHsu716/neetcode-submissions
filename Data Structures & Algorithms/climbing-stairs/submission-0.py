class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        pre1 = 2 
        pre2 = 1

        for i in range(3, n + 1):
            current = pre1 + pre2
            pre2 = pre1
            pre1 = current
        return pre1