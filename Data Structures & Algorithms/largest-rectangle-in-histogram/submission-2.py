class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        area = 0
        
        for i in range(len(heights)):
            miniheights = heights[i]
            for j in range(i, len(heights)):
                miniheights = min(miniheights, heights[j])
                weith = j - i + 1
                area = max(area, weith * miniheights)
        return area