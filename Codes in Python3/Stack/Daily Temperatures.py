#Using Stack
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n=len(temp)
        res=[0]*n
        st=[]
        for i in range(n):
            while st and temp[i]>temp[st[-1]]:
                idx=st.pop()
                res[idx]=i-idx
            st.append(i)
        return res

# TC=O(n)
# SC=O(n)

#Using DP
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n=len(temp)
        res=[0]*n
        st=[]
        for i in range(n-2,-1,-1):
            j=i+1
            #For a colder day in the future use the warmer index that 
            # day has
            while j<n and temp[j]<=temp[i]:
                if res[j]==0:
                    j=n
                    break
                j+=res[j]
            
            if j<n:
                res[i]=j-i

        return res

# TC=O(n)
# SC=O(1)

