
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen="",0

        for i in range(len(s)):
            #Odd Length
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if resLen <(r-l+1):
                    resLen=(r-l+1)
                    res=s[l:r+1]
                l-=1
                r+=1

            #Even Length
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if resLen <(r-l+1):
                    resLen=(r-l+1)
                    res=s[l:r+1]
                l-=1
                r+=1

        return res

# TC=O(n^2)
# SC=O(n)


        
# #Brute Force 
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         res, resLen="",0

#         for i in range(len(s)):
#             for j in range(i,len(s)):
#                 l,r=i,j
#                 while l<r and s[l]==s[r]:
#                     l+=1
#                     r-=1

#                 if l>=r and resLen <(j-i+1):
#                     res=s[i:j+1]
#                     resLen=(j-i+1)
#         return res

# # TC=O(n^3)
# # SC=O(n)
