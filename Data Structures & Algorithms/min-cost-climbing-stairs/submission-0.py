class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pre1 = cost[0]
        pre2 = cost[1]
        for i in range(2, len(cost)):
            cur = cost[i] + min(pre1, pre2)
            pre1 = pre2
            pre2 = cur
        return min(pre1, pre2)