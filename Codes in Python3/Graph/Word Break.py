#Bottom Up Solutiom
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:    
        dp=[False] * (len(s)+1)
        dp[len(s)]=True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                size=len(w)
                if i+size<=len(s) and s[i:i+size]==w:
                    dp[i]=dp[i+size]
                if dp[i]:
                    break
        
        return dp[0]

# TC=O(T*M*N)
    # Let N be the length of the string and 
    # M be the number of words in wordDict, and T max lenght of any word (as to compare)
# SC=O(N)

#Top Down Solutiom
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:    
        memo={len(s):True}
        def f(i):
            if i in memo:
                return memo[i]
            for w in wordDict:
                size=len(w)
                if i+size<=len(s) and s[i:i+size]==w:
                     if f(i+size):
                        memo[i]=True
                        return True
            memo[i] = False
            return memo[i]
        return f(0)

# TC=O(T*M*N)
    # Let N be the length of the string and 
    # M be the number of words in wordDict, and T max lenght of any word (as to compare)
# SC=O(N)

#Recursive Solutiom
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:    
        def f(i):
            if i==len(s):
                return True
            for w in wordDict:
                size=len(w)
                if i+size<=len(s) and s[i:i+size]==w:
                     if f(i+size):
                        return True
            return False
        return f(0)

# TC=O(T*(M^N))
    # Let N be the length of the string and 
    # M be the number of words in wordDict, and T max lenght of any word (as to compare)
# SC=O(N)