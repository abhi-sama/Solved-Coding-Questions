class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l,r=0,n-1
        while l<r:
            total=numbers[l]+numbers[r]
            if target==total:
                return [l+1,r+1]
            if total<target:
                l+=1
            else:
                r-=1
        
        return []
    
# TC=O(n)
# SC=O(1)