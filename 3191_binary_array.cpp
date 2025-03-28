#include <iostream>

using namespace std;

int solve(std::vector<int> nums) {
    int ans = 0;

    for (int i=0; i<nums.size(); i++) {
        if (nums[i] == 0) {
            if (i+2 >= nums.size()) return -1;

            ans += 1;
            nums[i] ^= 1;
            nums[i + 1] ^= 1;
            nums[i + 2] ^= 1;
        }
    }

    return ans;
}

int main() {
    cout << solve({0,1,1,1,0,0}) << endl;
    cout << solve({0,1,1,1}) << endl;
}
