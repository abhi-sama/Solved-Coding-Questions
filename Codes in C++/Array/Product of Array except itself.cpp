class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size());
        int prefix=1;
        int suffix=1;
        int n=nums.size();
        for(int i=0;i<n;i++){
            res[i]=prefix;
            prefix*=nums[i];  
        }
        for(int i=n-1;i>=0;i--){
            res[i]*=suffix;
            suffix*=nums[i];
        }
        return res;
    }
};