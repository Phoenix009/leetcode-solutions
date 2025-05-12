#include <iostream>

using namespace std;

int solve(vector<int> nums) {
    int ans = 0;
    for (int mask=0; mask<pow(2, nums.size()); mask++) {
        int acc = 0;
        for (int j = 0; j<nums.size(); j++) {
            if (mask & 1<<j) acc ^= nums[j];
        }
        ans += acc;
    }
    return ans;
}

int main() {
    cout << solve({1, 3}) << endl;
    cout << solve({5, 1, 6}) << endl;
    cout << solve({3,4,5,6,7,8}) << endl;
}
