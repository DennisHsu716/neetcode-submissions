class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top = 0
        botton = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while left <= right and top <= botton:
            
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, botton + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= botton:
                for i in range(right, left - 1, -1):
                    res.append(matrix[botton][i])
                botton -= 1
            
            if left <= right:
                for i in range(botton, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res 