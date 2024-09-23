#include <algorithm>
#include <iostream>

using namespace std;

int countPrimes(int n) {
    if (n < 3) return 0;

    bool bitmap[n];
    fill(bitmap, bitmap + n, true);

    bitmap[0] = false;
    bitmap[1] = false;

    int i = 0;
    int ans = 0;
    while (i < n) {
        if (bitmap[i] == true) {
            ans += 1;
            int j = 1;
            while (i * j < n) {
                bitmap[i * j] = false;
                j += 1;
            }
        }
        i += 1;
    }
    return ans;

}

int main() {
    cout << countPrimes(0) << endl;
    cout << countPrimes(1) << endl;
    cout << countPrimes(10) << endl;
    cout << countPrimes(100) << endl;

    return 0;
}
