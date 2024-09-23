#include <iostream>

using namespace std;

vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
    vector<int> pre = {0};
    for (auto val: arr) pre.push_back(pre.back() ^ val);

    vector<int> ans = vector<int>();
    for (auto query: queries) {
        int left = query.front() + 1;
        int right = query.back() + 1;
        int an = pre[left-1] ^ pre[right];
        ans.push_back(an);
    }

    return ans;
    
}

int main() {
    vector<int> arr = {1,3,4,8};
    vector<vector<int>> queries = {{0,1},{1,2},{0,3},{3,3}};
    vector<int> ans = xorQueries(arr, queries);
    for (auto an: ans) cout << an << " ";
    cout << endl;
    return 0;
}
