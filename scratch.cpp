#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    vector<int> arr = {12, 23, 35 ,1, 13, 354, 65412};
    sort(arr.begin(), arr.end(), greater<int>());
    for (auto item: arr) cout << item << " ";
    cout << endl;
}
