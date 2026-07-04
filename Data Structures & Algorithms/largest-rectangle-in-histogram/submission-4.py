class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            miniheights = heights[i]
            for j in range(i, len(heights)):
                weight = j - i + 1
                miniheights = min(miniheights, heights[j])
                area = max(area, miniheights * weight)

        return area