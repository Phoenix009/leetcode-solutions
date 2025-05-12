#include <algorithm>
#include <iostream>
#include <cmath>
#include <stdatomic.h>
#include <string>

using namespace std;

long long solve(long long start, long long finish, int limit, string k) {
    int num_digits = floor(log10(finish)) + 1;
    int num_digits_present = k.size();
    int num_digits_solve = num_digits - num_digits_present;
    
    if (num_digits_solve < 1) return -1;

    vector<int> dig_limits = vector<int>(num_digits_solve, 9);
    
    string finish_str = to_string(finish);
    reverse(finish_str.begin(),finish_str.end());
    for (int i=0; num_digits_present + i + 1 <= num_digits; i++){
        int digit = finish_str[num_digits_present + i] - '0';
        dig_limits[i] = min(digit, limit);
    }

    for (auto item: dig_limits) cout << item << " ";
    cout << endl;
    


    return 0ll;
}

int main() {
    cout << solve(1, 6000, 4, "4") << endl;
    cout << solve(15, 215, 6, "10") << endl;
    cout << solve(1000, 2000, 4, "3000") << endl;
}
