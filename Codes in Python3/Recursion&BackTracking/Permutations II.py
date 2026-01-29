# Optimal Approach
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=set()

        def bt(i):
            if i==len(nums):
                return 
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                nums[i],nums[j]=nums[j],nums[i]
                ans.add(tuple(nums.copy()))
                bt(i+1)
                nums[i],nums[j]=nums[j],nums[i]
        
        bt(0)
        return list(ans)
        
# TC=O(n!*n)
#     last n for copying the list
# SC=O(n!∗n)
#     last n for max recursion depth


# # Approach 1
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         ans=set()

#         def bt(i):
#             if i==len(nums):
#                 return 
#             for j in range(i,len(nums)):
#                 nums[i],nums[j]=nums[j],nums[i]
#                 ans.add(tuple(nums.copy()))
#                 bt(i+1)
#                 nums[i],nums[j]=nums[j],nums[i]
        
#         bt(0)
#         return list(ans)
        
# # TC=O(n!*n)
# #     last n for copying the list
# # SC=O(n!∗n)
# #     last n for max recursion depth