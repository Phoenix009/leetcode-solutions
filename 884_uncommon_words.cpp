#include <iostream>
#include <map>
#include <sstream>

using namespace std;

vector<string> uncommonFromSentences(string s1, string s2) {
    stringstream words1 = stringstream(s1);
    stringstream words2 = stringstream(s2);

    map<string, int> frq;
    string word;
    while (words1 >> word) {
        frq[word]++;
    }

    while (words2 >> word) {
        frq[word]++;
    }

    vector<string> ans;
    for (auto entry: frq) {
        if (entry.second == 1) ans.push_back(entry.first);
    }
    return ans;

}


int main() {
    string s1 = "This apple is sweet";
    string s2 = "This apple is sour";

    vector<string> ans = uncommonFromSentences(s1, s2);
    for (auto word: ans) cout << word << " ";
    cout << endl;
}
