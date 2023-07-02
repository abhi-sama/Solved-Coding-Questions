class Solution {
private:
    void recPermute(int index,vector<int>& nums,vector<vector<int>>&res)
    {
        if(index==nums.size())
            {res.push_back(nums);
            return;
            }
        for(int i=index;i<nums.size();i++)
        {
            swap(nums[index],nums[i]);
            recPermute(index+1,nums,res);
            swap(nums[index],nums[i]);
        }
        return;
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> res;
    recPermute(0,nums,res);
    return res;
    }
};