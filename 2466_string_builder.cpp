#include <iostream>

using namespace std;

void count_possiblities(int target_length, int current_length, int zero, int one, int& count) {
    if (target_length == current_length) {
        count++;
        return;
    }

    if (current_length + zero <= target_length) 
        count_possiblities(target_length, current_length + zero, zero, one, count);

    if (current_length + one <= target_length) 
        count_possiblities(target_length, current_length + one, zero, one, count);
}

int solve(int low, int high, int zero, int one) {
    const int MOD = 1e9 + 7;
    int ans = 0;
    
    for (int target_length = low; target_length <= high; target_length++) {
        int current_count = 0;
        count_possiblities(target_length, 0, zero, one, current_count);
        ans += current_count % MOD;
        ans %= MOD;
    }

    return ans;
}

int main() {
    cout << solve(3, 3, 1, 1) << endl;
    cout << solve(2, 3, 1, 2) << endl;
}
