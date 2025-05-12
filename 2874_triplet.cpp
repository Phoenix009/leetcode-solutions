#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long solve(vector<int> nums) {
  long long ans = 0;
  long long maxA = nums[0];
  long long maxAB = 0;
  for (int i=1; i<nums.size() - 1; i++) {
    maxAB = max(maxA - nums[i], maxAB);
    maxA = max(maxA, (long long)nums[i]);
    ans = max(ans, maxAB * nums[i+1]);
  }

  return ans;
}

int main() {
  cout << solve({12, 6, 1, 2, 7}) << endl;
  cout << solve({7, 10, 3, 4, 19}) << endl;
  cout << solve({1, 2, 3}) << endl;
}


