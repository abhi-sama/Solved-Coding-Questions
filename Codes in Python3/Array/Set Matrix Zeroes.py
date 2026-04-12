class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m=len(matrix),len(matrix[0])
        col0=1

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    # mark i-th row
                    matrix[i][0]=0
                    # mark j-th col 
                    if j!=0:
                        matrix[0][j]=0
                    else:
                        col0=0
        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]!=0:
                    if matrix[i][0]==0 or matrix[0][j]==0:
                        matrix[i][j]=0

        # Based on the 00 cell mark the first row
        if matrix[0][0]==0:
            for j in range(m):
                matrix[0][j]=0

                # Based on the 00 cell mark the first col
        if col0==0:
            for i in range(n):
                matrix[i][0]=0


# TC=O(nm)
# SC=O(1)
