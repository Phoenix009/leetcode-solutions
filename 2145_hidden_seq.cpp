#include <algorithm>
#include <iostream>

using namespace std;

int solve(vector<int> diff, int lower, int upper) {
    int mini = diff[0];
    int maxi = diff[0];
    int curr = diff[0];
    for (int i=1; i<diff.size(); i++) {
        curr += diff[i];
        mini = min(mini, curr);
        maxi = max(maxi, curr);
    }

    int ans = 0;
    for (int i=lower; i <= upper; i++) {
        if (
            lower <= mini + i && 
            upper >= mini + i && 
            lower <= maxi + i && 
            upper >= maxi + i
            ) ans++;
    }

    return ans;
}

int main() {
    cout << solve({1, -3, 4}, 1, 6) << endl << endl;
    cout << solve({3,-4,5,1,-2}, -4, 5) << endl << endl;
    cout << solve({4, -7, 2}, 3, 6) << endl << endl;
}
