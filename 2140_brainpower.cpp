#include <iostream>

using namespace std;

long long solve(vector<vector<int>> questions) {
    vector<long long> dp = vector<long long>(questions.size()+1, 0ll);

    for (int i=questions.size()-1; i>-1; i--) {
        auto item = questions[i];
        int score = item[0];
        int skips = item[1] + 1;

        // if we do solve this question
        if (i + skips < dp.size()) score += dp[i + skips];

        dp[i] = max(dp[i+1], 1ll *score);
    }

    // for (auto item: dp) std::cout << item << " ";
    // std::cout << std::endl;

    return dp[0];
}

int main() {
    cout << solve({{3,2},{4,3},{4,4},{2,5}}) << endl;
    cout << solve({{1,1},{2,2},{3,3},{4,4},{5,5}}) << endl;
}

