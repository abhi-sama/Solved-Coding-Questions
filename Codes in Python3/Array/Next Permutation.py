class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return
         
        while nums[j] <= nums[i-1]:
            j -= 1

        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        nums[i:]= nums[len(nums)-1:i-1:-1]
        '''
         the line nums[i:] = nums[len(nums)-1:i-1:-1]
        reverses the order of elements from index i to the end of the nums list.
        It updates the original nums list with the reversed elements, 
        while keeping the elements before index i unchanged.
        sequence[start(inclusive):stop(exclusive):step]
        
        '''
