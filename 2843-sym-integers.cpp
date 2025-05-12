#include <iostream>
#include <string>

using namespace std;

bool is_valid(int num) {
    string num_str = to_string(num);
    if (num_str.size() % 2) return false;
    int half_index = num_str.size() / 2;

    int first_half_sum = 0;
    int second_half_sum = 0;
    for (int i = 0; i<num_str.size(); i++) {
        if (i < half_index) first_half_sum += num_str[i] - '0';
        else second_half_sum += num_str[i] - '0';
    }
    return first_half_sum == second_half_sum;
}

int solve(int low, int high) {
    int count = 0;
    for (int i=low; i<=high; i++) {
        if (is_valid(i)) count++;
    }
    return count;
}

int main() {
    cout << solve(1, 100) << endl;
    cout << solve(1200, 1230) << endl;
}
