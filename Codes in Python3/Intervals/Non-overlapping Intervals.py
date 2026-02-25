#Sorting by Start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        intervals.sort(key=lambda i:i[0])
        prevEnd=intervals[0][1]
        for start,end in intervals[1:]:
            if prevEnd>start:
                count+=1
                prevEnd=min(prevEnd,end)
            else:
                prevEnd=end

        return count

# TC=O(nlogn)
# SC=O(n)

#Sorting by End
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        intervals.sort(key=lambda i:i[1])
        prevEnd=intervals[0][1]
        for i in range(1, len(intervals)):
            if prevEnd>intervals[i][0]:
                count+=1
            else:
                prevEnd=intervals[i][1]

        return count

# TC=O(nlogn)
# SC=O(n)