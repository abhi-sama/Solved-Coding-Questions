class Solution {
public:
    vector<int> genRow(int row)
    {
        long long ans=1;
        vector<int> ansRow;
        ansRow.push_back(1);
        for(int col=1;col<row;col++)
        {
            ans=ans*(row-col);
            ans=ans/col;
            ansRow.push_back(ans);
        }
        return ansRow;
    }
    vector<vector<int>> generate(int numRows) {
    vector<vector<int>> res;
    /*
         for(int i=0;i<numRows;i++)
         {  
             vector<int> temp(i+1,1);
             for(int j=1;j<i;j++)
             {
              temp[j]=res[i-1][j-1]+res[i-1][j];
             }            
            res.push_back(temp);
         }
        */
    for(int row=1;row<=numRows;row++)
    {
        res.push_back(genRow(row));
    }
    return res;
    }
};