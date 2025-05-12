#include <iostream>
#include <unordered_map>

using namespace std;

long long solve(vector<int> nums, int modulo, int k) {
    long long ans = 0;
    int current_count = k;
    unordered_map<int, int> frq{};
    frq[current_count] = 1;

    for (auto item: nums) {
        current_count += item % modulo == k;
        ans += frq[current_count % k]++;
    }

    return ans;
}


int main() {
    cout << solve({3, 2, 4}, 2, 1) << endl;
    cout << solve({3, 1, 9, 6}, 3, 0) << endl;
}
