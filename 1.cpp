#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

int solve(string server_health) {
    vector<int> count {};
    vector<char> nums {};

    for (auto item: server_health) {
        if (nums.empty()) {
            nums.push_back(item);
            count.push_back(0);
        }

        if (nums.back() == item) count.back()++;
        else {
            nums.push_back(item);
            count.push_back(1);
        }
    }

    for (auto item: count) cout << item << endl;
}

int main() {
    cout << solve("001100") << endl;
    cout << solve("11010")<< endl;

}
