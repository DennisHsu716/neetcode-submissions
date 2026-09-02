class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        pre1 = cost[0]
        pre2 = cost[1]

        for i in range(2, n):
            curr = cost[i] + min(pre1, pre2)
            pre1 = pre2
            pre2 = curr
        return min(pre1, pre2)