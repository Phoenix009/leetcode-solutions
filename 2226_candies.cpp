#include <iostream>

using namespace std;

bool is_valid(int guess, vector<int> &candies, long long k) {
  int count = 0;
  for (auto candy : candies) {
    count += candy / guess;
  }
  return count >= k;
}

int solve(vector<int> candies, long long k) {
  int ans = 0;
  int left = 0;
  int right = *max_element(candies.begin(), candies.end());
  while (left <= right) {
    int mid = left + (right - left) / 2;
    if (is_valid(mid, candies, k)) {
      ans = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return ans;
}

int main() {
  cout << solve({5, 8, 6}, 3) << endl;

  cout << solve({2, 5}, 11) << endl;

  return 0;
}
