class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        if self.left and self.right:
            if self.right and -self.left[0] > self.right[0]:
                left = heapq.heappop(self.left)
                heapq.heappush(self.right, -left)
        
        if len(self.left) > len(self.right) + 1:
            left = heapq.heappop(self.left)
            heapq.heappush(self.right, -left)
        elif len(self.right) > len(self.left) + 1:
            right = heapq.heappop(self.right)
            heapq.heappush(self.left, -right)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.left) < len(self.right):
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2
        
        