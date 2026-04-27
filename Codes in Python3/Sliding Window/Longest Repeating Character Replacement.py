#Sliding Window(Optimal)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        l=0
        count={}
        maxF=0

        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            maxF=max(maxF,count[s[r]])

            while (r-l+1)-maxF>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        
        return res

# TC=O(n)
# SC=O(m)


#Sliding Window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        charSet=set(s)

        for c in charSet:
            count=l=0
            for r in range(len(s)):
                if s[r]==c:
                    count+=1
                
                while (r-l+1)-count>k:
                    if s[l]==c:
                        count-=1
                    l+=1
                
                res=max(res,r-l+1)
        
        return res

# TC=O(m*n)
# SC=O(m)