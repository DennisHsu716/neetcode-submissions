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
                    weidth = i - stack[-1] - 1
                else:
                    weidth = i
                
                area = max(area, weidth * miniheights)
            stack.append(i)
        return area