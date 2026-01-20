#Solution 2 Iterative
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        if not digits:
            return res
        res=[""]
        digitSet={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        for digit in digits:
            temp=[]
            for curStr in res:
                for ch in digitSet[digit]:
                    temp.append(curStr+ch)
            res=temp
        return res
# TC=O(n*4^n)
# SC=O(n*4^n)
#Solution 2
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         digitSet={
#             "2":"abc",
#             "3":"def",
#             "4":"ghi",
#             "5":"jkl",
#             "6":"mno",
#             "7":"pqrs",
#             "8":"tuv",
#             "9":"wxyz"
#         }
#         res=[]

#         def backtrack(i,curStr):
#             if len(curStr)==len(digits):
#                 return res.append(curStr)
#             for ch in digitSet[digits[i]]:
#                 backtrack(i+1,curStr+ch)
#         if digits:
#             backtrack(0,"")

#         return res
# # TC=O(n*4^n)
# # SC=O(n*4^n)