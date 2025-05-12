#include <iostream>

using namespace std;

bool solve(vector<int> arr) {
    int count = 0;
    for (auto item: arr) {
        if (item % 2) count++;
        else count = 0;
        if (count == 3) return true;
    }
    return false;
}

int main() {
    cout << solve({2, 6, 4, 1}) << endl;
    cout << solve({1,2,34,3,4,5,7,23,12}) << endl;
}
