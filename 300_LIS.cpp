#include <algorithm>
#include <iostream>

using namespace std;

int lengthOfLIS(vector<int>& nums) {
    vector<int> dp = vector<int>(nums.size(), 1);
    for(int i=1; i<nums.size(); i++) {
        for(int j=0; j<i; j++) {
            if (nums[i] > nums[j])
                dp[i] = max(dp[i], dp[j] + 1);
        }
    }

    return *max_element(dp.begin(), dp.end());
}

int main() {
    vector<int> nums = {10,9,2,5,3,7,101,18};
    cout << lengthOfLIS(nums) << endl;
}

