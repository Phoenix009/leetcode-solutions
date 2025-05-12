#include <iostream>

using namespace std;

vector<int> solve(vector<int> nums) {
    vector<int> ans{};
    for (int i=0; i<nums.size(); i++) {
        ans.push_back(nums[nums[i]]);
    }
    return ans;
}

int main() {
    vector<int> ans = solve({0, 2, 1, 5, 3, 4});
    for (auto item: ans) cout << item << " " ;
    cout << endl;

    ans = solve({5, 0, 1, 2, 3, 4});
    for (auto item: ans) cout << item << " " ;
    cout << endl;
}
