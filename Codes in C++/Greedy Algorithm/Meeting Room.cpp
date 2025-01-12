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
    static bool comp(const Interval& x, const Interval& y){
       return x.start<y.start; 
    }
    bool canAttendMeetings(vector<Interval>& intervals) {
        sort(intervals.begin(),intervals.end(),comp);
        for(int i=1;i<intervals.size();i++){
            if(intervals[i].start<intervals[i-1].end) return false;
        }
        return true;
    }
};
