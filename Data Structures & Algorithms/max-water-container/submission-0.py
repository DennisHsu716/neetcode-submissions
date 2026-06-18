class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        high = len(heights) - 1
        low = 0

        while low < high:
            heigh = min(heights[low], heights[high])
            weight = high - low
            res = max(res, weight * heigh)
        
            if heights[low] < heights[high]:
                low += 1
            else:
                high -= 1
        return res 