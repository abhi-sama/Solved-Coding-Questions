class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, 
    int sr, int sc, int color) {
        int m=image.size();
        int n=image[0].size();
        queue<pair<int,int>> q;
        int dr[]={-1,0,+1,0};
        int dc[]={0,+1,0,-1};
        int init_color=image[sr][sc];
        q.push({sr,sc});
        while(!q.empty())
        {
            int r=q.front().first;
            int c=q.front().second;
            image[r][c]=color;
            q.pop();
            for(int i=0;i<4;i++)
            {
                int nrow=r+dr[i];
                int ncol=c+dc[i];
                if(nrow>=0 && nrow<m && 
                ncol>=0 && ncol<n && 
                image[nrow][ncol]==init_color&&
                image[nrow][ncol]!=color)
                {
                    q.push({nrow,ncol});
                }
            }
        }
        return image;
    }
};