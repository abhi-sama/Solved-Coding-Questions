class Solution {
public:
    int majorityElement(vector<int>& nums) {
    int n=nums.size();
    int voter=0;
	int votes=1;
	for(int i=1;i<n;i++)
	{	if(votes==0)
		{
			votes=1;
			voter=i;
		}
		else if(nums[voter]==nums[i])
			votes++;
		else votes--;
	}
	int count=0;
	for(int i=0;i<n;i++)
	{
		if(nums[i]==nums[voter])
		count++;
	}
	return count>n/2?nums[voter]:-1;
    }
};