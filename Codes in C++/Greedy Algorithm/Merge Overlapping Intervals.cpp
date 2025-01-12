class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        sort(intervals.begin(), intervals.end());
        res.push_back(intervals[0]);
        for (auto interval : intervals) {
            int start = interval[0];
            int end = interval[1];
            int lastEnd = res.back()[1];
            if (start <= lastEnd) {
                res.back()[1] = max(lastEnd, end);
            } else {
                res.push_back({start, end});
            }
        }
        return res;
    }
};

// class Solution {
// public:
//     vector<vector<int>> merge(vector<vector<int>>& intervals) {
//     int n=intervals.size();
//     vector<vector<int>> res;
//     sort(intervals.begin(),intervals.end());
//     for(int i=0;i<n;i++)
//     {
//         if(res.empty()||res.back()[1]<intervals[i][0])
//             res.push_back({intervals[i][0],intervals[i][1]});
//         else
//             res.back()[1]=max(res.back()[1],intervals[i][1]);
//     }
//     return res;
//     }
// };