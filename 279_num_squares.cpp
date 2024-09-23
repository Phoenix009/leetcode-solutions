#include <cmath>
#include <iostream>

using namespace std;

int numSquares(int n) {
    int N = sqrt(n);
    vector<vector<int>> dp = vector<vector<int>>(N+1, vector<int>(n+1, 0));

    for(int j=1; j<n+1; j++)
        dp[1][j] = j;
    
    for (int i=2; i<N+1; i++) {
        for(int j=1; j<n+1; j++) {
            if (j < i*i) dp[i][j] = dp[i-1][j];
            else {
                dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-i*i]);
            }
        }
    }

    return dp[N][n];

}

int main() {
    cout << numSquares(12) << endl;
    cout << numSquares(13) << endl;
    return 0;
}
