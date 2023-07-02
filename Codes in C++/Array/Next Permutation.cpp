class Solution {
public:
    void nextPermutation(vector<int>& permutation) {
    int index=-1;
    int n=permutation.size();
    for(int i=n-2;i>=0;i--)
    {
        if(permutation[i]<permutation[i+1])
        {
            index=i;
            break;
        }
    }
    if(index==-1)
    {   reverse(permutation.begin(),permutation.end());
        return ;
    }
    for(int i=n-1;i>=0;i--)
    {
        if(permutation[i]>permutation[index])
         {
             swap(permutation[i],permutation[index]);
             break;
         }
    }
    reverse(permutation.begin()+index+1,permutation.end());
    }
};