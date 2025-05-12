#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solve(string s) { 
    vector<int> dp = vector<int>(s.size());

    unordered_map<char, int> store {};
    for (int i = s.size()-1; i > -1; i--) {
        if (store.count(s[i])) dp[i] = store[s[i]];
        else {
            dp[i] = i;
            store[s[i]] = i;
        }
    }
    
    vector<int> ans = vector<int>();
    int idx = 0;
    while (idx < s.size()) {
        int end = dp[idx];
        int j = idx;
        while (j <= end) {
            end = max(end, dp[j]);
            j++;
        }
        ans.push_back(end - idx + 1);
        idx = end + 1;
    }

    return ans;
}

int main() {
    vector<int> ans = solve("ababcbacadefegdehijhklij");
    for (auto item: ans) std::cout << item << " " ;
    std::cout << std::endl;

    ans = solve("eccbbbbdec");
    for (auto item: ans) std::cout << item << " " ;
    std::cout << std::endl;
}
