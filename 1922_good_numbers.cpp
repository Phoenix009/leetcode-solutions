#include <iostream>

using namespace std;

const int MOD = 1e9 + 7;

// Function to compute (a^b) % m using modular exponentiation
int modPower(long long a, long long b, int m) {
    long long res = 1;
    a %= m;
    while (b > 0) {
        if (b & 1)
            res = (res * a) % m;
        b >>= 1;
        a = (a * a) % m;
    }
    return (int)res;
}

int solve(long long n) {
    if (n == 0) return 0;

    long long half_up = (n + 1) / 2;
    long long half_down = n / 2;

    int num_even = modPower(5, half_up, MOD);
    int num_odd = modPower(4, half_down, MOD);

    long long ans = (1LL * num_even * num_odd) % MOD;
    return (int) ans;
}

int main() {
    cout << solve(1) << endl;   // Output: 5
    cout << solve(4) << endl;   // Output: 400
    cout << solve(50) << endl;  // Output: large number without overflow
}

