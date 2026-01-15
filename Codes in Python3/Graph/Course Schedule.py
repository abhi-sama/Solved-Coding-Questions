class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        adj=[[] for i in range(numCourses)]
        for src, dest in prerequisites:
            adj[dest].append(src)
            indegree[src]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        topo=[]
        while q:
            node=q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return len(topo)==numCourses 
    # TC=O(E+V)
    # SC=O(E+V)