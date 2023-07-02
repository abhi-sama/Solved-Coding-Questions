class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
    int n=nums.size();
    int ele1=INT_MIN;	int votes1=0;
    int ele2=INT_MIN;	int votes2=0;
	for(int i=0;i<n;i++)
	{	if(votes1==0&&nums[i]!=ele2)
		{
			votes1=1;
			ele1=nums[i];
		}
        else if(votes2==0&&nums[i]!=ele1)
		{
			votes2=1;
			ele2=nums[i];
		}
		else if(ele1==nums[i])
			votes1++;
        else if(ele2==nums[i])
			votes2++;
		else {votes1--;votes2--;}
	}
	int count1=0;
    int count2=0;
    vector<int> lis;

	for(int i=0;i<n;i++)
	{
		if(nums[i]==ele1)
		count1++;
        if(nums[i]==ele2)
		count2++;
	}
    cout<<ele1<<ele2;

    int mini=(int)(n/3);
    cout<<endl<<mini;
    if(count1>mini)
    lis.push_back(ele1);
    if(count2>mini)
    lis.push_back(ele2);
    cout<<endl<<count1<<endl<<count2;
	return lis;
    }
};