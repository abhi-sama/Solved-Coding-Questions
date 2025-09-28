# Psuedocode:
#     1) Iterate through length of the first string of array(taken arbitrarely) for in range len(strs[0])
#     2) For each string str in string array
#             if (i==len(str)) or str[i]!=strs[0][i]
#                 return str[:i]
#         return strs[0]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return s[:i]
        # strs = ["apple", "apple", "apple"] , below line reaches in this condition
        return strs[0]