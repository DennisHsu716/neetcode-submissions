class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue 
                
                nums = board[i][j]
                box_idx = (i // 3) * 3 + (j // 3)

                if nums in row[i]:
                    return False 
                
                if nums in col[j]:
                    return False 
                
                if nums in box[box_idx]:
                    return False 
                
                row[i].add(nums)
                col[j].add(nums)
                box[box_idx].add(nums)
        return True 