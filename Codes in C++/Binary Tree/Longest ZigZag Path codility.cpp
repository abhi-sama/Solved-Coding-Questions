int solve(tree* T,int count,int dir){
    int max=count;
    if(T==NULL) return 0;
    if(T->l!=NULL){
        int newCount=count;
        if(dir==1)newCount++;
        max=std::max(solve(T->l,newCount,-1),max);
    }
    if(T->r!=NULL){
        int newCount=count;
        if(dir==-1)newCount++;
        max=std::max(solve(T->r,newCount,1),max);
        
    }
    return max;
}

int solution(tree * T) {
    if(T==NULL) return 0;
   return solve(T,0,0);
}