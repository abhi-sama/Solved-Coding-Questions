class Solution {
public:
    static bool comp(vector<int>& a , vector<int>& b){
        if(a[1] == b[1]){
            return a[0]<b[0];
        }
        return a[1] < b[1];
    }
    int eraseOverlapIntervals(vector<vector<int>>& v) {
        sort(v.begin(),v.end(),comp);
        int res=0;
        int lastEnd=INT_MIN;
        for(int i=0;i<v.size();i++)
        {
            if(lastEnd>v[i][0])
            {
                res++;
            }
            else {
                lastEnd=v[i][1];
            }
        }
        return res;
    }
};