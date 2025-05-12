#include <iostream>
#include <limits>

using namespace std;

int get_cost(vector<int>& tops, vector<int>& bottoms, int value) {
    int cost = 0;
    for (int index=0; index<tops.size(); index++) {
        if (tops[index] == value) continue;
        else if (bottoms[index] == value) cost++;
        else return -1;
    }

    return cost;
}

int solve(vector<int> tops, vector<int> bottoms) {
    int ans = numeric_limits<int>::max();
    for (int value=1; value<7; value++) {
        int cost = get_cost(tops, bottoms, value);
        if (cost == -1) continue;
        ans = min(ans, cost);

        cost = get_cost(bottoms, tops, value);
        if (cost == -1) continue;
        ans = min(ans, cost);
    }

    if (ans == numeric_limits<int>::max()) return -1;
    return ans;

    return 0;
}

int main() {
  cout << solve({2, 1, 2, 4, 2, 2}, {5, 2, 6, 2, 3, 2}) << endl;
  cout << solve({3, 5, 1, 2, 3}, {3, 6, 3, 3, 4}) << endl;
}
