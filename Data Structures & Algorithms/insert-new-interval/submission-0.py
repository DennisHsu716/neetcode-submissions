class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for start, end in intervals:
            #left
            if end < newInterval[0]:
                res.append([start, end])
            #right 
            elif start > newInterval[1]:
                res.append(newInterval)
                newInterval = [start, end]
            #combine
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
        res.append(newInterval)
        return res