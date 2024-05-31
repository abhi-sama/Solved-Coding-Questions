class Solution {
public:
    int maxProfit(vector<int>& s) {
        int mini=s[0];
        int profit=0;
        int n=s.size();
        for(int i=1;i<n;i++)
        {
            int cost=s[i]-mini;
            profit=max(profit,cost);
            mini=min(mini,s[i]);
        }
        return profit;
    }
};