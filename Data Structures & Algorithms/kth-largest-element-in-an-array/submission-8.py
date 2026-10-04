class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        self.k = k
        res = []

        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > self.k:
                heapq.heappop(heap)
        return heap[0]