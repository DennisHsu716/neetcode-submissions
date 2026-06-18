class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = []
        area = 0
        for i in range(len(heights)):
            miniheights = heights[i]
            for j in range(i, len(heights)):
                miniheights = min(miniheights, heights[j])
                weight = j - i + 1
                area = max(area, miniheights * weight)
        return area