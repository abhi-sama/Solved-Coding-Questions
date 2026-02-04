#DFS Hashset
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(list)

        for prereq,crs in prerequisites:
            adj[crs].append(prereq)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs]=set()
                for prereq in adj[crs]:
                    prereqMap[crs]|=dfs(prereq) # "|" this means there is an Union Operation 
                prereqMap[crs].add(crs)
            return prereqMap[crs]
        
        prereqMap={}
        for crs in range(numCourses):
            dfs(crs)
        
        res=[]
        for u,v in queries:
            res.append(u in prereqMap[v])

        return res

# TC=O(V*(V+E)+m) #First V for union
# SC=O(V^2 + (E+V) +m )
# {Adjacency List } (V+E) + {Prerequisite Map } (V^2) + {Result Array } (m)$$
        

#Brute Force DFS (Fails)
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=[[] for _ in range(numCourses)]
        
        for u,v in prerequisites:
            adj[u].append(v)

        def dfs(src,target):
            if src==target:
                return True
            for nei in adj[src]:
                if dfs(nei,target):
                    return True
            return False

        res=[]
        for src,target in queries:
            res.append(dfs(src,target))
        return res

# TC=O((E+V)*m)
# SC=O(E+V)

# Where E is nos edges, V is nos vertices and m is nos queries