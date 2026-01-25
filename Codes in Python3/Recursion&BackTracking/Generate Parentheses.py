#Backtracking 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def backtrack(openN,closeN,s:str):
            if openN==closeN==n:
                return res.append(s)
            if openN<n:
                backtrack(openN+1,closeN,s+"(")
            if closeN<openN:         
                backtrack(openN,closeN+1,s+")")          

        backtrack(0,0,"")
        return res

# TC=O((4^n)/n^(1/2))
# SC=O(n)

# #Brute Force
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res=[]

#         def valid(s:str):
#             open=0
#             for c in s:
#                 open+=1 if c=="(" else -1
#                 if open<0:
#                     return False
#             return not open

#         def dfs(s:str):
#             if 2*n==len(s):
#                 if valid(s):
#                     res.append(s)
#                 return 
#             dfs(s + "(")
#             dfs(s + ")")

#         dfs("")
#         return res

# # TC=O(2^(2n)*n)
# # SC=O(2^(2n)*n)
        