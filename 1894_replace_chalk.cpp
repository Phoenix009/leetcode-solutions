#include <iostream>

using namespace std;

int chalkReplacer(vector<int>& chalk, int k) {
    long long sum = 0;
    for (auto value: chalk) sum += value;

    k %= sum;

    for (int i=0; i<chalk.size(); i++) {
        if (k < chalk[i]) return i;
        k -= chalk[i];
    }

    return -1;

}

int main() {
    vector<int> chalk = {3,4,1,2};
    int k=25 ;
    cout << chalkReplacer(chalk, k) << endl;
    return 0;
}

