class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l,r=0,n-1
        maxArea=0
        while l<r:
            area=min(heights[l],heights[r])*(r-l)
            maxArea= area if area>maxArea else maxArea
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            
        return maxArea

# TC=O(n)
# SC=O(1)
        