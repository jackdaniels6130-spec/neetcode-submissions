class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for row in board:
            cleaned_row = [i for i in row if i != '.']
            if len(cleaned_row) != len(set([i for i in row if i != "."])):
                return False
            
        # columns
        for i in range(len(board)):
            col = []
            for j in range(len(board)):
                col.append(board[j][i])
            cleaned_col = [i for i in col if i != '.']
            if len(cleaned_col) != len(set(cleaned_col)):
                return False

        # 3x3
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                grid = [] 
                for n in range(i, i+3):
                    for m in range(j, j+3):
                        grid.append(board[n][m])
                cleaned_grid = [i for i in grid if i != '.']
                if len(cleaned_grid) != len(set(cleaned_grid)):
                        return False
        return True
              