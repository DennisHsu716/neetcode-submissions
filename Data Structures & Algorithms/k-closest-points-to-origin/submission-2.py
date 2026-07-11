class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        count = []
        heap = []
        res = []

        for x, y in points:
            count = x*x + y*y
            heapq.heappush(heap, (count, [x, y]))
        
        for i in range(k):
            ideal, point = heapq.heappop(heap)
            res.append(point)
        return res 