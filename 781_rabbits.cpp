#include <iostream>
#include <map>

using namespace std;

int solve(vector<int> answers) {
    int ans = 0;

    map<int, int> frq {};
    for (auto item: answers) {
        frq[item]++;
    }

    for (auto [key, value]: frq) {
        int limit = ceil((double)value / (key + 1));
        ans += 1ll * limit * (key+1);
    }
    return ans;
}

int main() {
    cout << solve({1, 1, 2}) << endl;
    cout << solve({10, 10, 10}) << endl;
}

// n: n+1 then add n+1 to the count
// n: count < n + 1 then add n + 1 to the count, as they all could refer to each
//      other. 
// n: count > n + 1 then add ceil(value / key+1) * (key + 1). As only n+1
//      rabbits can refer to themselves, other extra should have different color
