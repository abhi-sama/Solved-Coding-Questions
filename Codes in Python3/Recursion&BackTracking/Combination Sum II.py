class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=set()
        candidates.sort()
        cur=[]

        def dfs(i,sum):
            if target==sum:
                res.add(tuple(cur))
                return
            if i>=len(candidates) or sum>target:
                return 
            #include candidates[i]
            cur.append(candidates[i])
            dfs(i+1,sum+candidates[i])
            cur.pop()
            #skip candidates
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,sum)

        dfs(0,0)
        return [list(combo) for combo in res]
    
# TC=O(n.2^n)
# SC=O(n)