# Using BucketSort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets=[[] for _ in range(len(nums)+1)]

        for num,freq in count.items():
            buckets[freq].append(num)
        
        res=[]
        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                res.append(num)
                if len(res)==k:
                    return res
        
# TC=O(n)
# SC=O(n)

# Using MinHeap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num, cnt in count.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

# TC=O(nlogk)
# SC=O(n+k)


#Using Sorting
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        arr=[]
        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort()
        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res

# TC=O(nlogn)
# SC=O(n)