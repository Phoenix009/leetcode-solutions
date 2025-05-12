#include <iostream>
#include <numeric>
#include <algorithm>

using namespace std;

bool solve(vector<int> nums) {
    int sum = accumulate(nums.begin(), nums.end(), 0);
    if (sum%2) return false;

    int target = sum / 2;

    vector<vector<bool>> dp = vector<vector<bool>>(nums.size(), vector<bool>(target+1, false));
    for (int i = 0; i<nums.size(); i++) dp[i][0] = true;
    dp[0][nums[0]] = true;

    for (int i=1; i<nums.size(); i++) {
        for (int j=1; j<=target; j++) {
            dp[i][j] = dp[i-1][j];
            if (j-nums[i] > -1 && dp[i-1][j - nums[i]]) dp[i][j] = true;
        }
    }
    return dp[nums.size()-1][target];
}

int main() {
    cout << solve({1,5,11,5}) << endl;
    cout << solve({1,2,3,5}) << endl;
}
