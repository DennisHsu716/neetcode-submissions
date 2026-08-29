class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        res = 0

        for i in range(len(gas)):
            res += gas[i] - cost[i]
            if res < 0:
                start = i + 1
                res = 0
        return start 