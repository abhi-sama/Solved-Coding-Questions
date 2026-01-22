 class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        return max(self.solve(nums[:-1]),self.solve(nums[1:]))

    def solve(self, houses: List[int]) -> int:
        if not houses:
            return 0
        if len(houses)==1:
            return houses[0]
        
        memo = [0] * len(houses)
        prev2=houses[0]
        prev=max(houses[0],houses[1])

        for i in range(2,len(houses)):
            cur=max(prev,houses[i]+prev2)
            prev2=prev
            prev=cur

        return prev

        # TC=O(n)
        # SC=O(n)

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums)==1:
#             return nums[0]
        
#         return max(self.solve(nums[:-1]),self.solve(nums[1:]))

#     def solve(self, houses: List[int]) -> int:
#         if not houses:
#             return 0
#         if len(houses)==1:
#             return houses[0]
        
#         memo = [0] * len(houses)
#         memo[0]=houses[0]
#         memo[1]=max(houses[0],houses[1])

#         for i in range(2,len(houses)):
#             memo[i]=max(memo[i-1],houses[i]+memo[i-2])

#         return memo[-1]

#         # TC=O(n)
#         # SC=O(n)

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums)==1:
#             return nums[0]
#         def dfs(houses):
#             memo={}
#             def solve(i):
#                 if i>=len(houses):
#                     return 0
#                 if i in memo:
#                     return memo[i]
#                 memo[i]=max(solve(i+1),houses[i]+solve(i+2))
#                 return memo[i]
#             return solve(0)
        
#         return max(dfs(nums[:-1]),dfs(nums[1:]))
#         # TC=O(n)
#         # SC=O(n)

        