#MinHeap Solution
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        ans=[]
        for pt in points:
            x,y=pt[0],pt[1]
            dist= math.sqrt((x**2)+(y**2))
            minHeap.append((dist,pt))
        heapq.heapify(minHeap)
        i=0
        while i!=k:
            dist,pt=heapq.heappop(minHeap)
            ans.append(pt)
            i+=1

        return ans
        
# TC=O(n+k*logn)
# SC=O(n)