#include <iostream>
#include <queue>

using namespace std;

void print_state(vector<char>& state) {
    for (auto item: state) cout << item << " ";
    cout << endl;
}

string solve(string dominoes) {
    vector<char> current_state = vector<char>(dominoes.begin(), dominoes.end());
    vector<char> new_state = vector<char>(dominoes.size(), '.');

    vector<int> queue {};
    for (int index=0; index<dominoes.size(); index++) {
        if (dominoes[index] != '.')
            queue.push_back(index);
    }

    vector<int> new_queue{};
    while (queue.size()) {


        for (auto index: queue) {
            if (current_state[index] == 'R') {
                new_state[index] = '/';
                if (index + 1 < dominoes.size()) {
                    if (new_state[index + 1] == 'L') new_state[index + 1] = '.'; // cancel out
                    else if (new_state[index + 1] == '.') new_state[index + 1] = 'R'; // falls to right
                    new_queue.push_back(index + 1);
                }
            }
            else if (current_state[index] == 'L') {
                new_state[index] = '\\';
                if (index - 1 > -1) {
                    if (new_state[index - 1] == 'R') new_state[index - 1] = '.'; // cancel out
                    else if (new_state[index - 1] == '.') new_state[index - 1] = 'L'; // falls to right
                    new_queue.push_back(index - 1);
                }
            }
        }

        current_state = new_state;

        queue = new_queue;
        new_queue.clear();
    }

    string result(dominoes.size(), '.');
    for (int index=0; index<dominoes.size(); index++) {
        if (current_state[index] == '/') result[index] = 'R';
        else if (current_state[index] == '\\') result[index] = 'L';
    }

    return result;
}

int main() {
    cout << solve("RR.L") << endl;
    cout << solve(".L.R...LR..L..") << endl;
    // vector<int> first = {1, 2, 3, 4, 5};
    // vector<int> second;
    // second = first;
    //
    // first.clear();
    // for (auto item: second) cout << item << " ";
    // cout << endl;
}
