class Solution {
public:
    bool checkInclusion(string s1, string s2) {
     if(s1.size()>s2.size())
        return false;
      vector<int> s1cnt(26,0);
      vector<int> s2cnt(26,0);
      for(int i=0;i<s1.size();i++){
        s1cnt[s1[i]-'a']++;
        s2cnt[s2[i]-'a']++;
      }
      int matches=0;
      for(int i=0;i<26;i++){
        if(s1cnt[i]==s2cnt[i])
            matches++;
      }
      int l=0;
      for(int r=s1.length();r<s2.length();r++){
        if(matches==26)return true;
        int ind=s2[r]-'a';
        s2cnt[ind]++;
        if(s1cnt[ind]==s2cnt[ind])matches++;
        else if(s1cnt[ind]+1==s2cnt[ind])matches--;
        ind=s2[l]-'a';
        s2cnt[ind]--;
        if(s1cnt[ind]==s2cnt[ind])matches++;
        else if(s1cnt[ind]-1==s2cnt[ind])matches--;
        l++;
      }
    return matches==26;
    }
};
