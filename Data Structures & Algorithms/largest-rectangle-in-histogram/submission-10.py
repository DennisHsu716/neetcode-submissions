class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []

        for i in range(len(heights) + 1):
            if i == len(heights):
                current = 0
            else:
                current = heights[i]

            while stack and current < heights[stack[-1]]:
                miniheights = heights[stack.pop()]

                if stack:
                    weigth = i - stack[-1] - 1
                else:
                    weigth = i

                area = max(area, weigth * miniheights)
            stack.append(i)
        return area 

