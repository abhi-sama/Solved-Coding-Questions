class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> freq(26, 0);
        for (char c : tasks)
            freq[c - 'A']++;
        sort(freq.begin(), freq.end());
        int maxFreq = freq[25];
        int gadhe = maxFreq - 1;
        int idleSpots = n * gadhe;
        for (int i = 24; i >= 0; i--) {
            idleSpots -= min(freq[i], gadhe);
        }
        if (idleSpots > 0)
            return tasks.size() + idleSpots;
        return tasks.size();
    }
};
// class Solution {
// public:
//     int leastInterval(vector<char>& tasks, int n) {
//         vector<int> freq(26, 0);
//         for (char c : tasks)
//             freq[c - 'A']++;
//         priority_queue<int> pq;
//         for (int x : freq) {
//             if (x > 0)
//                 pq.push(x);
//         }
//         int cnt = 0;
//         while (!pq.empty()) {
//             vector<int> temp;
//             for (int i = 1; i <= n + 1; i++) {
//                 if (!pq.empty()) {
//                     int eleLeft = pq.top();
//                     pq.pop();
//                     eleLeft--;
//                     temp.push_back(eleLeft);
//                 }
//             }
//             for (int x : temp) {
//                 if (x > 0)
//                     pq.push(x);
//             }

//             if (pq.empty())
//                 cnt += temp.size();
//             else
//                 cnt += n + 1;
//         }
//         return cnt;
//     }
// };