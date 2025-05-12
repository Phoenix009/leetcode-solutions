#include <iostream>
#include <cmath>
#include <algorithm>
#include <unordered_set>

using namespace std;

long long solve(int n, int k) {
    unordered_set<string> store {};
    int digit_length = n;
    for (int i=1; i < pow(10, digit_length/2); i++) {

        //construct the palindrome
        string first_half = to_string(i);
        string second_half = first_half;
        reverse(second_half.begin(), second_half.end());
        string final = first_half + second_half;
        long number = stoi(final);

        // if not k palindromic continue
        if (number % k) continue;

        sort(final.begin(), final.end());
        store.insert(final);
    }

    for (auto item: store) cout << item << " ";
    cout << endl;
    return 0ll;
}

int main() {
    cout << solve(3, 5) << endl;
    cout << solve(1, 4) << endl;
    cout << solve(5, 6) << endl;
}


