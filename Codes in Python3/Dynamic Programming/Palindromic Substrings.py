class Solution:
    def countSubstrings(self, s: str) -> int:
        psCount=[0]

        def expand_substring(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                psCount[0]+=1
                l-=1
                r+=1
        for i in range(len(s)):
            expand_substring(i,i)
            expand_substring(i,i+1)

        return psCount[0]
# TC=O(n^2)
# SC=O(1)
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         psCount=0
#         for i in range(len(s)):
#             #Odd length string
#             l,r=i,i
#             while l>=0 and r<len(s) and s[l]==s[r]:
#                 psCount+=1
#                 l-=1
#                 r+=1
#             l,r=i,i+1
#             while l>=0 and r<len(s) and s[l]==s[r]:
#                 psCount+=1
#                 l-=1
#                 r+=1

#         return psCount