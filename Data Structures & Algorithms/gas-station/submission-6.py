class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 
        task = 0
        start = 0

        for i in range(len(gas)):
            task += gas[i] - cost[i]
            if task < 0:
                start = i + 1
                task = 0
        return start