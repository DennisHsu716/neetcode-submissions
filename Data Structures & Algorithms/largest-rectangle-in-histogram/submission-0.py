class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = []
        area = 0
        for i in range(len(heights)):
            miniheight = heights[i]
            for j in range(i, len(heights)):
                weight = j - i + 1
                miniheight = min(miniheight, heights[j])
                area = max(area, weight * miniheight)
        return area