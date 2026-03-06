class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r

        while l<=r:
            k=(l+r)//2
            totalTime=0
            for p in piles:
                totalTime+=math.ceil(float(p)/float(k))
            if totalTime<=h:
                res=k
                r=k-1
            else:
                l=k+1
        return res

# TC=O(nlogm)
# SC=O(1)