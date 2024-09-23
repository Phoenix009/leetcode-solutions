#include <algorithm>
#include <iostream>

using namespace std;

int longestSubarray(vector<int>& nums) {
    int maxi = *max_element(nums.begin(), nums.end());
    int ans = 0;

    int count = 0;
    for (auto val: nums){
        if (val == maxi) count++;
        else count = 0;
        ans = max(ans, count);
    }

    return ans;
}

int main() {
    vector<int> nums = {1,2,3,3,2,2};
    cout << longestSubarray(nums) << endl;
}
