class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        /*
                int len = nums.size();
        for (int num : nums) {
            int idx = abs(num);
            if (nums[idx] < 0) {
                return idx;
            }
            nums[idx] = -nums[idx];
        }

        return len;
        */
        int slow=nums[0];
        int fast=nums[0];
        do{
        slow=nums[slow];
        fast=nums[nums[fast]];
        }while(slow!=fast);
        fast=nums[0];
        while(slow!=fast)
        {
            slow=nums[slow];
            fast=nums[fast];
        }
        return slow;
    }
};