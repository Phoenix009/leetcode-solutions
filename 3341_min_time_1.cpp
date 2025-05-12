#include <iostream>
#include <limits>

using namespace std;

int solve(vector<vector<int>> move_time) {
    // This is a solution for the case where we can only move right and down
    int num_rows = move_time.size();
    int num_cols = move_time[0].size();

    vector<vector<int>> dp = vector<vector<int>>(
        num_rows, 
        vector<int>(num_cols, numeric_limits<int>::max())
    );
    dp[0][0] = 0;

    for (int j = 1; j<num_cols; j++) {
        dp[0][j] = max(dp[0][j-1], move_time[0][j]) + 1;
    }

    for (int i = 1; i<num_rows; i++) {
        dp[i][0] = max(dp[i-1][0], move_time[i][0]) + 1;
    }

    for (int i=1; i<num_rows; i++) {
        for (int j=1; j<num_cols; j++) {
            int from_top = max(dp[i-1][j], move_time[i][j]) + 1;
            int from_left = max(dp[i][j-1], move_time[i][j]) + 1;

            dp[i][j] = min(from_top, from_left);
        }
    }

    return dp[num_rows-1][num_cols-1];
}

int main() {
    cout << solve({{0, 4}, {4, 4}}) << endl;
    cout << solve({{0, 0, 0}, {0, 0, 0}}) << endl;
    cout << solve({{0, 1}, {1, 2}}) << endl;
    cout << solve({{17, 56}, {97, 80}}) << endl;
}
