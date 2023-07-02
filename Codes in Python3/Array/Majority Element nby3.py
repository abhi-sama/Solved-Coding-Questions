  class Solution:
  	def majorityElement(self, nums: List[int]) -> List[int]:
  		candidates = {}
  		k = 3
  		for num in nums:
  			if num in candidates:
  				candidates[num] += 1
  			elif len(candidates) < k:
  				candidates[num] = 1
  			else:
  				temp={}
  				for c in candidates:
  					candidates[c]-=1
  					if candidates[c] >= 1:
  						temp[c] = candidates[c]
  				candidates = temp
  		out = [k for k in candidates if nums.count(k) > len(nums) // 3]          
  		return out