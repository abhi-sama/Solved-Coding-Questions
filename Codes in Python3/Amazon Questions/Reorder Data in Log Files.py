class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs,key=self.sort)
    
    def sort(self,logs):
        a,b=logs.split(' ',1)
        if b[0].isalpha():
            return (0,b,a)
        else:
            return (1,None,None)

    # TC=O(M.N.logN), where M is the max length of the a log, since comparision b/w two keys can take O(M)
    # SC=O(M.N), to keep the keys for sorting the logs.