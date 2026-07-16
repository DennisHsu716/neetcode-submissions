class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        time = 0
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start > res[-1][1]:
                res.append([start, end])
            else:
                end = min(end, res[-1][1])
                time += 1
        return time 
