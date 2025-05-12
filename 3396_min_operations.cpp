#include <cmath>
#include <iostream>
#include <unordered_set>

using namespace std;

int solve(vector<int> nums) {
    int count = 0;
    unordered_set<int> visited {};

    for (int i=nums.size()-1; i>-1; i--) {
        if (visited.count(nums[i])) break;
        visited.insert(nums[i]);
        count++;
    }

    int remaining = nums.size() - count;
    int steps = ceil((float) remaining / 3);
    return steps;
}

int main() {
    cout << solve({4, 2, 3, 3, 5, 7}) << endl;
    cout << solve({4, 5, 6, 4, 4}) << endl;
    cout << solve({6, 7, 8, 9}) << endl;
}
