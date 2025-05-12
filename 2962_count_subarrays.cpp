#include <algorithm>
#include <iostream>

using namespace std;

long long solve(vector<int> nums, int k) {
    int maxi = *max_element(nums.begin(), nums.end());
    int frq = 0;
    long long ans = 0;

    int start = 0, end = 0;
    for (end=0; end<nums.size(); end++) {
        frq += nums[end] == maxi;
        while (frq >= k) {
            frq -= nums[start] == maxi;
            start++;
        }
        ans += start;
    }
    return ans;
}

int main() {
  // cout << solve({1, 3, 2, 3, 3}, 2) << endl;
  // cout << solve({1, 4, 2, 1}, 3) << endl;
  cout << solve({61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82}, 2) << endl;
}
