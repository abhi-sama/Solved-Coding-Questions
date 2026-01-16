class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res=[]
        adj=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        q=deque()

        for dest,src in prerequisites:
            adj[src].append(dest)
            indegree[dest]+=1

        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            node=q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)

        return res if len(res)==numCourses else []       
        
    # TC=O(E+V)
    # SC=O(E+V)