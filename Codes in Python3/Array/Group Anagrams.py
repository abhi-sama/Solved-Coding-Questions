#Using Hashing
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())

# TC=O(m*n)
# SC=O(m*n)

#Using Sorting
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            sortedS=''.join(sorted(s))
            res[sortedS].append(s)
        
        return list(res.values())

# TC=O(m*nlogn)
# SC=O(m*n)
