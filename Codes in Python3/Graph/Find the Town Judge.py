# Psuedocode:-
# 1)Create a indegree array for all the people in the town.
# 2)If the town judge exist his indegree will be equal to (n-1) otherwise there isn o town judge
#  and hence return -1


# Approach 1
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # incoming=defaultdict(int)
        # outgoing=defaultdict(int)
        delta=defaultdict(int)

        for src,dst in trust:
            delta[src]-=1
            delta[dst]+=1

        for i in range(1,n+1):
            if delta[i]== n-1:
                return i
        
        return -1  
# Approach 2
# class Solution:
#     def findJudge(self, n: int, trust: List[List[int]]) -> int:
#         incoming=defaultdict(int)
#         outgoing=defaultdict(int)

#         for src,dst in trust:
#             outgoing[src]+=1
#             incoming[dst]+=1

#         for i in range(1,n+1):
#             if incoming[i]== n-1 and outgoing[i]==0:
#                 return i
        
#         return -1  