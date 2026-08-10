class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for i in range(len(heights) + 1):
            if i == len(heights):
                current = 0
            else:
                current = heights[i]
            
            while stack and current < heights[stack[-1]]:
                miniheights = heights[stack.pop()]
                
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = max(area, width * miniheights)
            stack.append(i)
        return area