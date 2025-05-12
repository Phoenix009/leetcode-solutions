#include <iostream>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

#define MOD ((int)1e9 + 7)

int get_prime_score(int num) {
    int score = 0;

    if (num % 2 == 0) {
        score++;
        while (num % 2 == 0) num /= 2;
    }

    for (int div = 3; div * div <= num; div += 2) {
        if (num % div == 0) {
            score++;
            while (num % div == 0) num /= div;
        }
    }

    if (num > 1) score++;
    return score;
}

int mod_pow(int base, int exp, int mod) {
    long long res = 1;
    long long b = base;
    while (exp > 0) {
        if (exp & 1) res = (res * b) % mod;
        b = (b * b) % mod;
        exp >>= 1;
    }
    return (int)res;
}

int solve(vector<int> nums, int k) {
    int n = nums.size();
    vector<int> scores;
    for (int num : nums)
        scores.push_back(get_prime_score(num));

    // Monotonic stack to find left boundaries
    stack<int> st;
    vector<int> left_max_index(n);

    for (int i = 0; i < n; i++) {
        while (!st.empty() && scores[st.top()] < scores[i])
            st.pop();

        left_max_index[i] = st.empty() ? 0 : st.top() + 1;
        st.push(i);
    }

    // Monotonic stack to find right boundaries
    st = stack<int>();
    vector<int> right_max_index(n);

    for (int i = n - 1; i >= 0; i--) {
        while (!st.empty() && scores[st.top()] <= scores[i])
            st.pop();

        right_max_index[i] = st.empty() ? n - 1 : st.top() - 1;
        st.push(i);
    }

    // Max-heap of (value, index)
    priority_queue<pair<int, int>> max_heap;
    for (int i = 0; i < n; i++)
        max_heap.push({nums[i], i});

    long long ans = 1;
    while (!max_heap.empty() && k > 0) {
        auto [val, idx] = max_heap.top();
        max_heap.pop();

        int l = left_max_index[idx];
        int r = right_max_index[idx];
        int length = (idx-l+1) * (r-idx+1);

        int times = min(k, length);
        int acc = mod_pow(val, times, MOD);

        ans = (ans * acc) % MOD;
        k -= times;
    }

    return (int)ans;
}

int main() {
    cout << solve({8, 3, 9, 3, 8}, 2) << endl;
    cout << solve({19, 12, 14, 6, 10, 18}, 3) << endl;
    return 0;
}

