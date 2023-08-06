class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ED=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1) + 1):
            ED[i][0] = i
        for j in range(len(word2) + 1):
            ED[0][j] = j
        for i,x in enumerate(word1):
            for j,y in enumerate(word2):
                if x==y:
                    ED[i+1][j+1]=ED[i][j]
                else:
                    ED[i+1][j+1]=min(ED[i][j],ED[i+1][j],ED[i][j+1])+1
        return ED[len(word1)][len(word2)]