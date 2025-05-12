#include <iostream>
#include <string>

using namespace std;

int solve(vector<int> nums) {
    int ans = 0;
    for (int num: nums) {
        ans += to_string(num).size() % 2 == 0;
    }
    return ans;
}

int main() {
    cout << solve({12,345,2,6,7896}) << endl;
    cout << solve({555,901,482,1771}) << endl;
}
