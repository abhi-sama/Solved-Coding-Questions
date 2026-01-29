class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        ans=[]

        def bt(i):
            if len(res)==k:
                return ans.append(res.copy())

            for j in range(i,n+1):
                res.append(j)
                bt(j+1)
                res.pop()
        
        bt(1)
        return ans

# TC=O(k*[n!/(n-k)!k!])
#         first k for copying each element
# SC=O(k*[n!/(n-k)!k!]) 
#         including the output array