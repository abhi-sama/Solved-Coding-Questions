class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        prev=[0]*n
        cur=[0]*n
        for i in range(n):
            prev[i]=matrix[0][i]
        for i in range(1,m):
            for j in range(0,m):
                u=matrix[i][j]+prev[j]
                ld=matrix[i][j]
                if j-1>=0:
                    ld+=prev[j-1]
                else:
                    ld+=float('inf')
                rd=matrix[i][j]
                if j+1<n:
                    rd+=prev[j+1]
                else:
                    rd+=float('inf')
                cur[j]=min(u,min(ld,rd))
            prev=cur
        mini=prev[0]
        for i in range(1,n):
            mini=min(mini,prev[i])
        return mini
                
