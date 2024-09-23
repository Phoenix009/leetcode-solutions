#include <iostream>

using namespace std;

int get_repr(string word) {
    int repr = 0;
    for(auto alpha:word) {
        repr |= 1 << (alpha - 'a');
    }
    return repr;
}

int countConsistentStrings(string allowed, vector<string>& words) {
    int alpha = ~get_repr(allowed);
    int count = 0;

    for (auto word: words) {
        int repr = get_repr(word);
        if (alpha & repr) count++;
    }
    return words.size() - count;
    
}

int main() {
    vector<string> words = {"ad","bd","aaab","baa","badab"};
    string allowed = "ab";
    
    cout << countConsistentStrings(allowed, words) << endl;


}

