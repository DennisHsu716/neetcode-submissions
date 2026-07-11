class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.store = []
        self.k = k

        for i in nums:
            heapq.heappush(self.store, i)

            if len(self.store) > self.k:
                heapq.heappop(self.store)        

    def add(self, val: int) -> int:
        heapq.heappush(self.store, val)

        if len(self.store) > self.k:
            heapq.heappop(self.store)
        
        return self.store[0]
        
