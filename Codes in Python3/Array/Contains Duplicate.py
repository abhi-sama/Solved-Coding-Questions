#Using Hash Set
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))<len(nums)
# TC=O(n)
# SC=O(n)
        
        