
#include <iostream>
#include <map>

using namespace std;

std::pair<int, int> get_dominant(vector<int> &nums) {
  int length = nums.size();

  map<int, int> frq = map<int, int>();
  for (auto num : nums)
    frq[num]++;

  for (auto item : frq) {
    if (item.second > length / 2)
      return item;
  }

  return {-1, 0};
}

int solve(vector<int> nums) {
  std::pair<int, int> dominant = get_dominant(nums);

  if (dominant.first == -1)
    return -1;

  // cout << "Dominant: " << dominant.first << " Count: " << dominant.second << endl;

  int count_dominant = 0;
  int left_length = 0;
  int total_length = nums.size();

  for (auto num : nums) {
    left_length++;
    if (num == dominant.first)
      count_dominant++;

    int right_length = total_length - left_length;
    int right_count = dominant.second - count_dominant;

    // cout << "left: " << left_length << " " << count_dominant << endl;
    // cout << "right: " << right_length << " " << right_count << endl;

    if ((count_dominant > left_length / 2) & (right_count > right_length / 2))
      return left_length - 1;
  }

  return -1;
}

int main() {
  cout << solve({1, 2, 2, 2}) << endl;
  cout << solve({2, 1, 3, 1, 1, 1, 7, 1, 2, 1}) << endl;
  cout << solve({3, 3, 3, 3, 7, 2, 2}) << endl;
}
