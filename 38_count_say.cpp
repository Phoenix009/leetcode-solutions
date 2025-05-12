#include <iostream>
#include <string>

using namespace std;

string count_and_say(string input) {
    string output = "";
    int index = 1, count = 1;
    char curr_char = input[0];

    while (index < input.size()) {
        if (curr_char != input[index]) {
            output += to_string(count) + curr_char;
            count = 0;
            curr_char = input[index];
        }
        count++;
        index++;
    }
    output += to_string(count) + curr_char;
    return output;
}


string solve(int n) {
    if (n == 1) return "1";
    string res = solve(n-1);
    res = count_and_say(res);
    return res;
}

int main() {
    cout << solve(4) << endl;
    cout << solve(1) << endl;
    cout << solve(30) << endl;
}
