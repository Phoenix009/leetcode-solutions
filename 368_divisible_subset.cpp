#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;

vector<int> solve(vector<int> nums) {
    sort(nums.begin(), nums.end());

    vector<int> dp = vector<int>(nums.size(), 1);
    vector<int> prev = vector<int>(nums.size(), -1);

    int max_index = 0;
    for (int j=0; j<nums.size(); j++) {
        for (int i=0; i<j; i++) {
            if (nums[j] % nums[i] == 0 && dp[j] < dp[i] + 1) {
                dp[j] = dp[i] + 1;
                prev[j] = i;
            }
        }
        if (dp[j] > dp[max_index]) {
            max_index = j;
        }
    }
    

    vector<int> ans {};
    ans.push_back(nums[max_index]);
    while (prev[max_index] != -1) {
        max_index = prev[max_index];
        ans.push_back(nums[max_index]);
    }

    return ans;

}

int main() {
    vector<int> sol = solve({1, 2, 3});
    for (auto item: sol) cout << item << " ";
    cout << endl;

    sol = solve({1, 2, 4, 8});
    for (auto item: sol) cout << item << " ";
    cout << endl;
}
