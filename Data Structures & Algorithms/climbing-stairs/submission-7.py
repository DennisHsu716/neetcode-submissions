class Solution:
    def climbStairs(self, n: int) -> int:
        pre1 = 1
        pre2 = 2

        for i in range(3, n + 1):
            curr = pre1 + pre2
            pre1 = pre2
            pre2 = curr
        return pre2