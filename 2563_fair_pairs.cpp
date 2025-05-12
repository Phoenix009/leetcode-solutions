#include <algorithm>
#include <iostream>

using namespace std;

long long solve(vector<int> nums, int lower, int upper) {
    long long ans = 0;
    sort(nums.begin(), nums.end());
    for (auto item: nums) cout<< item << " ";
    cout << endl;

    for (auto item: nums) {
        int small = lower - item;
        int big = upper - item;
        int left = lower_bound(nums.begin(), nums.end(), small) - nums.begin();
        int right =  upper_bound(nums.begin(), nums.end(), big) - nums.begin() - 1;
        cout << item << ": " << small << " " << big << " " << left << " " << right << endl;

        ans += right - left + 1;
        if (item >= small && item <= big) ans -= 1;
    }
    
    return ans / 2;
}

int main() {
    cout << solve({0, 1, 7, 4, 4, 5}, 3, 6) << endl;
    cout << solve({1, 7, 9, 2, 5}, 11, 11) << endl;
    cout << solve({0, 0, 0, 0, 0, 0}, 0, 0) << endl;
}
