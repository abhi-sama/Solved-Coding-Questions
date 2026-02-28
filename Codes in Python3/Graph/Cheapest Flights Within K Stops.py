#Shortest Path Faster Algorithm
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float("inf")]*n
        prices[src]=0
        adj = [[] for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])
        
        q=deque([(0,src,0)]) #cost,node,stops
        while q:
            cost,node,stops=q.popleft()
            if stops>k:
                continue
            for nei,w in adj[node]:
                if cost+w<prices[nei]:
                    prices[nei]=cost+w
                    q.append((cost+w,nei,stops+1))
        
        return -1 if prices[dst]==float('inf') else prices[dst]

# TC=O(n.k)
# SC=O(n+m)

#Bellman Ford
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float("inf")]*n
        prices[src]=0

        for i in range(k+1):
            tmpPrices=prices.copy()
            for s,d,p in flights:
                if prices[s]==float('inf'):
                    continue
                if prices[s]+p<tmpPrices[d]:
                    tmpPrices[d]=prices[s]+p
            prices=tmpPrices
        
        return -1 if prices[dst]==float('inf') else prices[dst]

# TC=O(E.k)
# SC=O(n)