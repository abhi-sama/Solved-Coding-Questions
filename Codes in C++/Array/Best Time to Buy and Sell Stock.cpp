class Solution {
public:
    int maxProfit(vector<int>& prices) {
      int n=prices.size();
      int buy=prices[0];
      int sell=0;
      for(int i=0;i<n;i++)
      {
          buy=min(buy,prices[i]);
          sell=max(sell,prices[i]-buy);
      }
     /*vector<int> diff(n-1,1);
      int currSum=0;int maxSum=0;
      for(int i=0;i<n-1;i++)
      {
          diff[i]=prices[i+1]-prices[i];
      }
     //Kadane's Algo
     int startIndex=0;
     for(int i=0;i<n-1;i++)
     {
        if(currSum+diff[i]>0)
            currSum+=diff[i];
        else currSum=0;
         if(currSum>maxSum)
         maxSum=currSum;
     }*/
      return sell;
    }
};