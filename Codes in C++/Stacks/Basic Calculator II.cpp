//Optimised Approach without stack
class Solution {
public:
    int calculate(string s) {
        int currNum = 0;
        int lastNum = 0;
        char opr = '+';
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            if (isdigit(c))
                currNum = currNum * 10 + (c - '0');
            if (!isdigit(c) && c != ' ' || i == s.length() - 1) {
                if (opr == '+' || opr == '-') {
                    ans += lastNum;
                    lastNum = (opr == '+') ? currNum : -currNum;
                } else if (opr == '*') {
                    lastNum = lastNum * currNum;
                } else if (opr == '/') {
                    lastNum = lastNum / currNum;
                }
                opr = c;
                currNum = 0;
            }
        }
        ans += lastNum;
        return ans;
    }
};
// class Solution {
// public:
//     int calculate(string s) {
//         int num = 0;
//         char opr = '+';
//         stack<int> st;
//         for (int i = 0; i < s.length(); i++) {
//             char c = s[i];
//             if (isdigit(c))
//                 num = num * 10 + (c - '0');
//             if (!isdigit(c) && c != ' ' || i == s.length() - 1) {
//                 if (opr == '+')
//                     st.push(num);
//                 else if (opr == '-')
//                     st.push(-num);
//                 else if (opr == '*') {
//                     num = st.top() * num;
//                     st.pop();
//                     st.push(num);
//                 } else if (opr == '/') {
//                     num = st.top() / num;
//                     st.pop();
//                     st.push(num);
//                 }
//                 opr = c;
//                 num = 0;
//             }
//         }
//         int ans = 0;
//         while (!st.empty()) {
//             ans += st.top();
//             st.pop();
//         }
//         return ans;
//     }
// };