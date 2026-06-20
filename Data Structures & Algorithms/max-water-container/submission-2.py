class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        left = 0
        right = n - 1

        while left < right:
            height = min(heights[left], heights[right])
            weight = right - left
            res = max(res, height * weight)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res 
