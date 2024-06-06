class Solution {
public:
    long totalHours(vector<int>& v, int hourly) {
        long totalH = 0;
        for (int i = 0; i < v.size(); i++) {
            totalH += ceil((double)v[i] / (double)hourly);
        }
        return totalH;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1, high = *max_element(piles.begin(), piles.end());
        while (low <= high) {
            int mid = (low + high) / 2;
            long totalH = totalHours(piles, mid);
            if (totalH <= h) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
};