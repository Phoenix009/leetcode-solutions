#include <iostream>

using namespace std;

int solve(int days, vector<vector<int>> meetings) {
    sort(meetings.begin(), meetings.end());

    int total = 0;
    int start = 0, end = -1;
    for (auto meet : meetings) {
        if (meet[0] > end) {
            total += end - start + 1;
            start = meet[0];
            end = meet[1];
        } else {
            end = max(end, meet[1]);
        }
    }
    total += end - start + 1;
    return days - total;
}

int main() {
  cout << solve(10, {{5, 7}, {1, 3}, {9, 10}}) << endl;

  cout << solve(5, {{2, 4}, {1, 3}}) << endl;

  cout << solve(6, {{1, 6}}) << endl;
  return 0;
}
