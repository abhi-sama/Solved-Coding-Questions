# Using MinHeap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[]
        for num in nums:
            heapq.heappush(minHeap,num)

            if len(minHeap)>k:
                heapq.heappop(minHeap)
        
        return minHeap[0]

# TC=O(nlogk)
# SC=O(k)

# Using MaxHeap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap=nums
        heapq.heapify_max(nums)
        res= -1
        for i in range(k):
            res=heapq.heappop_max(maxHeap)
        
        return res

# TC=O(n+klogn)
# SC=O(1)