class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(lock):
            res=[]
            for i in range(4):
                digit=str((int(lock[i])+1)%10)
                res.append((lock[:i]+digit+lock[i+1:]))
                digit=str((int(lock[i])-1+10)%10)
                res.append((lock[:i]+digit+lock[i+1:]))                
            return res

        q=deque()
        q.append(("0000",0))
        visit=set(deadends) #O(m)

        while q:
            lock,turns=q.popleft()
            if lock==target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append((child,turns+1))

        return -1      

# TC=O(b^n+m)  
# SC=O(b^n+m) 
#     b-base of numbersytem
#     n- no of wheels
#     m- no of deadends
