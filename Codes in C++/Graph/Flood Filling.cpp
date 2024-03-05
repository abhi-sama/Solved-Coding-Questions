class Solution {
public:
    void dfs(vector<vector<int>>& image,vector<vector<int>>& ans, 
    int sr, int sc,int di[],int dj[],int init_color, int newColor)
    {
        int m=image.size();
        int n=image[0].size();
        ans[sr][sc]=newColor;
        for(int i=0;i<4;i++)
        {
         int nrow=sr+di[i];
         int ncol=sc+dj[i];
        if(nrow>=0&&nrow<m&&ncol>=0&&ncol<n&&image[nrow][ncol]==init_color&&ans[nrow][ncol]!=newColor)
         dfs(image,ans,nrow,ncol,di,dj,init_color,newColor);   
        }

    }

    vector<vector<int>> floodFill(vector<vector<int>>& image, 
    int sr, int sc, int color) {
        int m=image.size();
        int n=image[0].size();
        int init_color=image[sr][sc];
        vector<vector<int>> ans=image;
        int di[]={-1,0,+1,0};
        int dj[]={0,+1,0,-1};
        dfs(image,ans,sr,sc,di,dj,init_color,color);
        return ans;
    }
};