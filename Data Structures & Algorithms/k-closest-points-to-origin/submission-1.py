class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        count = 0


        for x, y in points:
            count = x*x + y*y
            heapq.heappush(heap, (count, [x, y]))
        
        for i in range(k):
            dist, point = heapq.heappop(heap)
            res.append(point)
        return res 
