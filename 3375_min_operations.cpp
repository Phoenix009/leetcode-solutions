#include <iostream>
#include <set>

using namespace std;

int solve(vector<int> nums, int k) {
    set<int> store {};
    for (auto num: nums) {
        if (num < k) return -1;
        if (num > k) store.insert(num);
    }
    return store.size();
}

int main() {
    cout << solve({5, 2, 5, 4, 5}, 2) << endl;
    cout << solve({2, 1, 2}, 2) << endl;
    cout << solve({9, 7, 5, 3}, 1) << endl;
}
