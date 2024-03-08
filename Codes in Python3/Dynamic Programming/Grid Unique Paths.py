class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev=[0]*(n)
        for i in range(m):
            temp=[0]*(n)
            for j in range(n):
                if i==0 and j==0:
                    temp[j]=1
                if(i>0):
                    temp[j]+=prev[j]
                if(j>0):
                    temp[j]+=temp[j-1]
            prev=temp
        return prev[n-1]
# SuperOptimalSolution
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         N=m+n-2
#         r=m-1
#         res=1
#         for i in range(0,r):
#             res=res*(N-i)
#             res=res//(i+1)
#         return res