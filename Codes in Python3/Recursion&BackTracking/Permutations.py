#Optimal Solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(ind):
            if ind==len(nums):
                return res.append(nums.copy())
            for i in range(ind,len(nums)):
                nums[ind],nums[i]=nums[i],nums[ind]
                backtrack(ind+1)
                nums[ind],nums[i]=nums[i],nums[ind]
        backtrack(0)
        return res

# TC=O(n!*n)
# SC=O(n!*n)

# #Solution 2
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         perms=[[]]
#         for n in nums:
#             new_perms=[]
#             for p in perms:
#                 for i in range(len(p)+1):
#                     p_copy=p.copy()
#                     p_copy.insert(i,n)
#                     new_perms.append(p_copy)
#             perms=new_perms
#         return perms
    
# # TC=O(n!*n^2) (n^2 for n insert operation each of n TC)
# # SC=O(n!*n)

# #Solution 3
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         if len(nums)==0:
#             return [[]]
#         res=[]
#         perm=self.permute(nums[1:])
#         for p in perm:
#             for i in range(len(p)+1):
#                 p_copy=p.copy()
#                 p_copy.insert(i,nums[0])
#                 res.append(p_copy)
#         return res
    
# # TC=O(n!*n^2) (n^2 for n insert operation each of n TC)
# # SC=O(n!*n)

        