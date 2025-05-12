#include <iostream>
#include <map>

using namespace std;


int solve(vector<vector<int>> dominoes) {
    map<pair<int, int>, int> frq {};
    int ans = 0;

    for (auto domino: dominoes) {
        if (domino[0] > domino[1]) {
            int temp = domino[1];
            domino[1] = domino[0];
            domino[0] = temp;
        }

        frq[{domino[0], domino[1]}]++;
        ans += frq[{domino[0], domino[1]}] - 1;
    }

    return ans;
    
}

int main() {
  cout << solve({{1, 2}, {2, 1}, {3, 4}, {5, 6}}) << endl;
  cout << solve({{1, 2}, {1, 2}, {1, 1}, {1, 2}, {2, 2}}) << endl;
}
