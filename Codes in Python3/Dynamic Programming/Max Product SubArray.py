class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre, suff, max_so_far = 0, 0, float('-inf')
        for i in range(len(nums)):
            pre = (pre or 1) * nums[i]
            suff = (suff or 1) * nums[~i]
            max_so_far = max(max_so_far, pre, suff)
        return max_so_far
