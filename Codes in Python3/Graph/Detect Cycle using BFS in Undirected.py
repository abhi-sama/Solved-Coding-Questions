class Solution:
    def isCycle(self,src,adj,vis)->bool:
        vis[src]=1
        q=[(src,-1)]
        while q:
            node,parent=q.pop(0)
            for adjacent in adj[node]:
                if vis[adjacent] is False:
                    vis[adjacent]=1
                    q.append((adjacent,node))
                elif parent!=adjacent:
                    return True
        return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        v = numCourses
        # adj = [[] for _ in range(v)]
        # for preq in prerequisites:
        #     adj[preq[0]].append(preq[1])

        # vis = [False] * v
        vis=[False for i in range(v)]
        for i in range(v):
            if vis[i] is False:
                if self.isCycle(i, prerequisites, vis):
                    return True
        return False
