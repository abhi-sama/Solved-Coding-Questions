class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*len(s)
        for i in range(len(s)):
            for word in wordDict:
                if i-len(word)+1<0:
                    continue
                if i==len(word)-1 or dp[i-len(word)]:
                    if s[i-len(word)+1:i+1]==word:
                        dp[i]=True
                        break   
        return dp[-1]
# ***********Top-Down Approach**************
# Apparently you don't need memoization variable while recursion if you use cache it does the same things
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         @cache
#         def dp(i):
#             if i < 0: 
#                 return True

#             for word in wordDict:
#                 if s[i - len(word) + 1:i + 1] == word and dp(i - len(word)):
#                     return True
            
#             return False
        
#         return dp(len(s) - 1)