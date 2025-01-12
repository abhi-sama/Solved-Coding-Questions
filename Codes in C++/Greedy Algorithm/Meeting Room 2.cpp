/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        vector<int> start;
        vector<int> end;
        for(auto x:intervals){
            start.push_back(x.start);
            end.push_back(x.end);
        }
        sort(start.begin(),start.end());
        sort(end.begin(),end.end());
        int min_rooms=0,cnt_rooms=0;
        int s=0,e=0;
        while(s<start.size()){
            if(start[s]<end[e]){
                cnt_rooms++;
                s++;
                min_rooms=max(min_rooms,cnt_rooms);
            }
            else{
                e++;
                cnt_rooms--;
            }
        }
        return min_rooms;
     }
};
