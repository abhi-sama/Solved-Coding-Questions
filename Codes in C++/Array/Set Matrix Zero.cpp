class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
   /* int x=0;
	int y=0;
	pair<int,int> p;
	stack<pair<int,int>> s;
	for(int i=0;i<matrix.size();i++)
	{
		for(int j=0;j<matrix[i].size();j++)
		{
			if(matrix[i][j]==0){
				x=i;
				y=j;
				p.first=x;
				p.second=y;
				s.push(p);
			}
		}
	}
	while(!s.empty())
	{
		p=s.top();
		s.pop();
		x=p.first;
		y=p.second;
		for(int cols=0;cols<matrix[x].size();cols++)
		matrix[x][cols]=0;
		for(int rows=0;rows<matrix.size();rows++)
		matrix[rows][y]=0;
	}
	return;*/
    int cols=matrix[0].size();
    int rows=matrix.size();
		int col0=1;
		for(int i=0;i<rows;i++)
		for(int j=0;j<cols;j++)
		{
			if(matrix[i][j]==0)
			{
				matrix[i][0]=0;

				if(j!=0)matrix[0][j]=0;
				else col0=0;
			
			}
		}

		for(int i=1;i<rows;i++)
		for(int j=1;j<cols;j++)
		{
			if(matrix[i][0]==0||matrix[0][j]==0)
				matrix[i][j]=0;
		}

		if(matrix[0][0]==0)
		for(int i=0;i<cols;i++)matrix[0][i]=0;
		if(col0==0)
		for(int i=0;i<rows;i++)matrix[i][0]=0;

    }
};