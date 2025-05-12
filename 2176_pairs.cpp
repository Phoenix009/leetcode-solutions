#include <iostream>

using namespace std;

int solve(vector<int> nums, int k) {
    int ans = 0;
    unordered_map<int, vector<int>> store{};
    for (int i=0; i<nums.size(); i++) {
        for (auto index: store[nums[i]])
            if ((i * index) % k == 0) ans++;
        store[nums[i]].push_back(i);
    }
    return ans;
}

int main() {
    cout << solve({3,1,2,2,2,1,3}, 2) << endl;
    cout << solve({1, 2, 3, 4}, 1) << endl;
}
