#include <iostream>
#include <string>

using namespace std;

int dp[10][2][80];

bool is_prime(int num) {
    if (num < 2) return false;
    for (int i=2; i<=num/2; i++) if (num%i == 0) return false;
    return true;
}

int get_ans(string& limit, int idx, bool bound, int sum) {
    if (idx == limit.size()) return is_prime(sum);
    if (dp[idx][bound][sum] != -1) return dp[idx][bound][sum];
    
    int range = (bound ? limit[idx] - '0' : 9);
    int ans = 0;
    for (int i=0; i<=range; i++) {
        ans += get_ans(
            limit, 
            idx+1, 
            bound && i==limit[idx] - '0', 
            sum+i
        );
    }
    dp[idx][bound][sum] = ans;
    return dp[idx][bound][sum];
}

int solve() {
    long left, right;
    cin >> left >> right;
    string left_str = to_string(left - 1), right_str = to_string(right);
    
    memset(dp, -1, sizeof(dp));
    int left_ans = get_ans(left_str, 0, 1, 0);

    memset(dp, -1, sizeof(dp));
    int right_ans = get_ans(right_str, 0, 1, 0);
    
    cout << right_ans - left_ans << endl;
    return 0;
}

int main() {
    int test_cases; cin >> test_cases;
    while (test_cases--) solve();
}
