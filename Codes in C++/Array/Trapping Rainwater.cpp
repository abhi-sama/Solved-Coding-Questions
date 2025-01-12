class Solution {
public:
    int trap(vector<int>& arr) {
        int n = arr.size();
        int lMax, rMax, l, r, total;
        total = lMax = rMax = 0;
        l = 0;
        r = n - 1;
        while (l < r) {
            if (arr[l] <= arr[r]) {
                if (lMax > arr[l])
                    total += lMax - arr[l];
                else
                    lMax = arr[l];
                l++;
            } else {
                if (rMax > arr[r])
                    total += rMax - arr[r];
                else
                    rMax = arr[r];
                r--;
            }
        }
        return total;
    }
};