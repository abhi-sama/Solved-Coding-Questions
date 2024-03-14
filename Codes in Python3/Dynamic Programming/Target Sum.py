class Solution:
    def findWays(self,num, tar):
        n = len(num)

        prev = [0] * (tar + 1)
        
        if num[0] == 0:
            prev[0] = 2  # 2 cases - pick and not pick
        else:
            prev[0] = 1  # 1 case - not pick
        
        if num[0] != 0 and num[0] <= tar:
            prev[num[0]] = 1  # 1 case - pick
        
        for ind in range(1, n):
            cur = [0] * (tar + 1)
            for target in range(tar + 1):
                notTaken = prev[target]
        
                taken = 0
                if num[ind] <= target:
                    taken = prev[target - num[ind]]
            
                cur[target] = (notTaken + taken)
            prev = cur
        return prev[tar]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        totSum = 0
        for i in range(n):
            totSum += nums[i]
        if totSum - target < 0 or (totSum - target) % 2:
            return 0
        return self.findWays(nums, (totSum - target) // 2)