class Solution {
public:
    int largestAltitude(vector<int>& gain) {
    int maxn=0;
    int sum=0;
    for(int i=0;i<gain.size();i++){
        sum=sum+gain[i];
        maxn=max(maxn,sum);
    }
    return maxn;
    }
};