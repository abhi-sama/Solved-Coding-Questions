class SmallestInfiniteSet {
public:
    SmallestInfiniteSet() {
       const int n=1000;
       for(int i=1;i<=n;i++)
        s.insert(i); 
    }
    
    int popSmallest() {
        const int min=*s.begin();
        s.erase(s.begin());
        return min;
    }
    
    void addBack(int num) {
      s.emplace(num);
    }
private: set<int> s;
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */