#Space Optimised Bottom Up Approach
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
            m,n=len(word1),len(word2)
            if m < n:
                m, n = n, m
                word1, word2 = word2, word1
            next_row=[0]*(n+1)

            for j in range(n+1):
                next_row[j]=n-j

            for i in range(m-1,-1,-1):
                curr_row=[0]*(n+1)
                curr_row[n]=m-i
                for j in range(n-1,-1,-1):
                    if(word1[i]==word2[j]):
                        curr_row[j]=next_row[j+1] #Do nothing
                        continue
                    else:
                        insert= curr_row[j+1] 
                        delete= next_row[j]
                        replace=next_row[j+1]
                        curr_row[j] =min(insert,delete,replace)+1
                next_row=curr_row
            return next_row[0]     

#TC=O((m*n))
#SC=O(min(m,n))


#Bottom Up Approach
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][n]=m-i
        for j in range(n+1):
            dp[m][j]=n-j

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if(word1[i]==word2[j]):
                    dp[i][j]=dp[i+1][j+1] #Do nothing
                    continue
                else:
                    insert= dp[i][j+1] 
                    delete= dp[i+1][j]
                    replace=dp[i+1][j+1]
                    dp[i][j] =min(insert,delete,replace)+1
        
        return dp[0][0]     

#TC=O((m*n))
#SC=O(m+n)


#Top Down Approach
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp=[[-1]*(n+1) for _ in range(m+1)]
        def f(i,j):
            if i==len(word1):
                return n-j
            if j==len(word2):
                return m-i
            if dp[i][j]!=-1:
                return dp[i][j]
            if(word1[i]==word2[j]):
                dp[i][j]=f(i+1,j+1) #Do nothing
                return dp[i][j] 
            else:
                insert= f(i,j+1) 
                delete= f(i+1,j)
                replace=f(i+1,j+1)
                dp[i][j] =min(insert,delete,replace)+1
            return dp[i][j] 
        
        return f(0,0)     

#TC=O((m*n))
#SC=O(m+n)

#Recursion
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        def f(i,j):
            if i==len(word1):
                return n-j
            if j==len(word2):
                return m-i
            
            if(word1[i]==word2[j]):
                return f(i+1,j+1) #Do nothing
            else:
                insert= f(i,j+1)
                delete= f(i+1,j)
                replace=f(i+1,j+1)
                res=min(insert,delete,replace)+1
            return res
        
        return f(0,0)          

#TC=O(3^(m+n))
#SC=O(m+n)
