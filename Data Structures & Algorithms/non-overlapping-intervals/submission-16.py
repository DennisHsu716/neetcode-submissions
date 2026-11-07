class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        time = 0
        prevend = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevend:
                prevend = end 
            else:
                time += 1
                prevend = min(prevend, end)
        return time 