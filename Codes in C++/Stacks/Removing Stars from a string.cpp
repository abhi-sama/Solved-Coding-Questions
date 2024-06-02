class Solution {
public:
    string removeStars(string s) {
        stack<char> st;
        string ans = "";
        for (char c : s) {
            if (c == '*')
                st.pop();
            else
                st.push(c);
        }
        while (!st.empty()) {
            ans.push_back(st.top());
            st.pop();
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }

    //     string removeStars(string s) {
    //     string t="";
    //     for(int i=0;i<s.length();i++){
    //         if(s[i]=='*')
    //         t.pop_back();
    //         else
    //         t.push_back(s[i]);
    //     }
    //     return t;
    // }
};