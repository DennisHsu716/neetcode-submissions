class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x:x[0])
        prevend = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevend:
                prevend = end
            else:
                prevend = min(prevend, end)
                count += 1
        return count 
                
        