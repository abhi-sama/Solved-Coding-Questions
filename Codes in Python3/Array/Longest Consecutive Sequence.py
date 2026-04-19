#Using Set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0
        
        for num in numSet:
            if (num-1) not in numSet:
                length=1
                while (num+length) in numSet:
                    length+=1
                longest=max(longest,length)
        return longest

# TC=O(n)
# SC=O(n)
    
#Using Sorting
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        hash=defaultdict(int)
        for num in nums:
            hash[num]+=1
        longest=0
        res=0
        lastKey=-float('inf')
        for key in hash:
            if lastKey+1==key:
                longest+=1
                lastKey=key
            else:
                lastKey=key
                longest=1
            if longest>res:
                res=longest

        return res

# TC=O(nlogn)
# SC=O(n)
        
        