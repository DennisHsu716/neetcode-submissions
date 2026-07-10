class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        count = 0
        heap = []
        res = []

        for x, y in points:
            count = x*x + y*y
            heapq.heappush(heap, (count, [x, y]))
        
        for i in range(k):
            dis, tex = heapq.heappop(heap)

            res.append(tex)
        return res