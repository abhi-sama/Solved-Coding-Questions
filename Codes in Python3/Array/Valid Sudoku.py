# #Solution 2 One Pass
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=defaultdict(set)
        rows=defaultdict(set)
        squares=defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if (board[r][c] in rows[r] 
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True

# TC=O(n^2)
# SC=O(n^2)


# #Solution 1
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         #For row validation
#         for row in range(9):
#             seen=set()
#             for i in range(9):
#                 if board[row][i]=='.':
#                     continue
#                 if board[row][i] in seen:
#                     return False
#                 seen.add(board[row][i])

#         #For column validation
#         for column in range(9):
#             seen=set()
#             for i in range(9):
#                 if board[i][column]=='.':
#                     continue
#                 if board[i][column] in seen:
#                     return False
#                 seen.add(board[i][column])

#         #For 3x3 Square Validation
#         for square in range(9):
#             seen=set()
#             for i in range(3):
#                 for j in range(3):
#                     row=(square//3)*3 + i
#                     col=(square%3)*3 + j
#                     if board[row][col]=='.':
#                         continue
#                     if board[row][col] in seen:
#                         return False
#                     seen.add(board[row][col])
        
#         return True
    
# # TC=O(n^2)
# # SC=O(n)