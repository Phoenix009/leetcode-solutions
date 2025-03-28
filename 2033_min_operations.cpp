#include <cstdlib>
#include <iostream>

using namespace std;

int find_steps(int x, vector<int> nums, int target) {
    int steps = 0;
    for (auto num: nums) {
        steps += abs(num - target) / x;
    }
    return steps;
}

int solve(vector<vector<int>> grid, int x) {
    int n = grid.size();
    int m = grid[0].size();
    
    int acc = grid[0][0] % x;
    vector<int> nums = vector<int>();

    for (auto row: grid) {
        for (auto ele: row) {
            if (ele % x != acc) return -1;
            nums.push_back(ele);
        }
    }

    sort(nums.begin(), nums.end());
    
    if (n*m % 2 == 1) {
        int median_index = n*m / 2;
        return find_steps(x, nums, nums[median_index]);
    } else {
        int median_index = n*m / 2;
        int ans = find_steps(x, nums, nums[median_index]);
        ans = min(ans, find_steps(x, nums, nums[median_index - 1]));
        return ans;
    }




}

int main() {
    cout << solve(
        {{2, 4}, {6, 8}},
        2
    ) << endl;

    cout << solve(
        {{1, 5}, {2, 3}},
        1
    ) << endl;

    cout << solve(
        {{1, 2}, {3, 4}},
        2
    ) << endl;
}
