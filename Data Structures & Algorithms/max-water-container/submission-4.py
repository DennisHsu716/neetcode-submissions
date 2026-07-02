class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        res = 0

        while left < right:
        #height 
            height = min(heights[left], heights[right])
        #weight 
            weight = right - left
        #res = h * w
            res = max(res, height * weight)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res