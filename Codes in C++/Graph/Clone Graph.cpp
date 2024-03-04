#include <bits/stdc++.h> 
/***************************************************************************

	Class for graph node is as follows:

	class graphNode
	{
		public:
    		int data;
    	vector<graphNode *> neighbours;
    	graphNode()
    	{
        	data = 0;
        	neighbours = vector<graphNode *>();
    	}

    	graphNode(int val)
    	{
        	data = val;
        	neighbours = vector<graphNode *>();
    	}

    	graphNode(int val, vector<graphNode *> neighbours)
    	{
        	data = val;
        	this->neighbours = neighbours;
    	}
	};

******************************************************************************/
graphNode *dfs(graphNode *node,map<graphNode*,graphNode*> &oldToNew)
{
    if(oldToNew.find(node)!=oldToNew.end())
        return oldToNew[node];
    graphNode* copy= new graphNode(node->data);
    oldToNew[node]=copy;
    for(auto nei:node->neighbours)
        copy->neighbours.push_back(dfs(nei,oldToNew));
    return copy;
}

graphNode *cloneGraph(graphNode *node)
{
    if(node==nullptr)
     return nullptr;
    map<graphNode*,graphNode*> oldToNew;
    return dfs(node,oldToNew);
}