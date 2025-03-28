#include <iostream>
#include <unordered_map>

using namespace std;




vector<int> sumPrefixScores(vector<string>& words) {
    
}

int main() {
    vector<string> words = {"abc","ab","bc","b"};
    vector<int> ans = sumPrefixScores(words);
    for (auto an: ans) cout << an << " ";
    cout << endl;
}
