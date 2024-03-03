class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        
        vector<vector<int>> total_sub;
        for(int i=0;i<pow(2,nums.size());i++)
        {  vector<int> subs;
            for(int j=0;j<nums.size();j++)
             {
                 if(i & (1<<j))
                  subs.push_back(nums[j]);
             }
             total_sub.push_back(subs);
        }
        return total_sub;
    }
};