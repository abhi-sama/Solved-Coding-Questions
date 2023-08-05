class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      m=len(text1)
      n=len(text2)
      LCS=[[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
      for i,x in enumerate(text1):
          for j,y in enumerate(text2):
              LCS[i+1][j+1]=LCS[i][j]+1 if x==y else max(LCS[i][j+1],LCS[i+1][j])
      return LCS[-1][-1]