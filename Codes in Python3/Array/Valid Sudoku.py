class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #For row validation
        for row in range(9):
            seen=set()
            for i in range(9):
                if board[row][i]=='.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        #For column validation
        for column in range(9):
            seen=set()
            for i in range(9):
                if board[i][column]=='.':
                    continue
                if board[i][column] in seen:
                    return False
                seen.add(board[i][column])

        #For 3x3 Square Validation
        for square in range(9):
            seen=set()
            for i in range(3):
                for j in range(3):
                    row=(square//3)*3 + i
                    col=(square%3)*3 + j
                    if board[row][col]=='.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True

