class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1] * len(queries)
        intervals.sort(key=lambda x:x[0])
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        heap = []
        i = 0

        for q, idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                left = intervals[i][0]
                right = intervals[i][1]
                length = right - left + 1

                heapq.heappush(heap, (length, right))
                i += 1
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                res[idx] = heap[0][0]
        return res 