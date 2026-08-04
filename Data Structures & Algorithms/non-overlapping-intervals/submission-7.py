class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        time = 0
        res = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= res:
                res = end
            else:
                res = min(res, end)
                time += 1
        return time 

