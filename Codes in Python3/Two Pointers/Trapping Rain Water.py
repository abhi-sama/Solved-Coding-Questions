class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        lMax,rMax=height[0],height[len(height)-1]
        maxArea=0

        while(l<r):
            if height[l]<height[r]:
                if lMax<height[l]:
                    lMax=height[l]
                else:
                    maxArea+=lMax-height[l]
                l+=1
            else:
                if rMax<height[r]:
                    rMax=height[r]
                else:
                    maxArea+=rMax-height[r]
                r-=1
        return maxArea

# TC=O(n)
# SC=O(1)