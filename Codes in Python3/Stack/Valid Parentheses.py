#Using Stack
class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for c in s:
            if c == '(' or c == '[' or c == '{':
                st.append(c)
            else:
                if not st or (c == ')' and st[-1] != '(') or (c == ']' and st[-1] != '[') or (c == '}' and st[-1] != '{'):
                    return False
                st.pop()
        return not st                    

# TC=O(n)
# SC=O(n)