#include <iostream>

using namespace std;

bool solve(vector<int> nums, vector<vector<int>> queries) {
    vector<int> dp = vector<int>(nums.size() + 1, 0);

    for (auto query: queries) {
        dp[query[0]] += 1;
        dp[query[1] + 1] -= 1;
    }

    for (int i=1; i<dp.size(); i++) {
        dp[i] += dp[i-1];
    }

    for (int i=0; i<nums.size(); i++) {
        if (nums[i] > dp[i]) return false;
    }

    return true;
}

int main() {
    cout << solve({1, 0, 1}, {{0, 2}}) << endl;
    cout << solve({4, 3, 2, 1}, {{1, 3}, {0, 2}}) << endl;
}
