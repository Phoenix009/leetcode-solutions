#include <iostream>

using namespace std;

int hIndex(vector<int>& citations) {
    int lo = 0;
    int hi = citations.size() - 1;
    int ans = 0;

    while (lo <= hi) {
        int mid = lo + (hi - lo)/2;
        if (citations[mid] >= mid + 1) {
            ans = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return ans;
}

int main() {
    vector<int> test1 = vector<int>({0,1,3,5,6});
    cout << hIndex(test1) << endl;
}

