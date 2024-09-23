#include <iostream>

using namespace std;

bool checkHIndex(vector<int>& citations, int hindex) {
    int count = 0;
    for (auto value: citations)
        count += value >= hindex;
    
    return count >= hindex;
}

int hIndex(vector<int>& citations) {
    int lo = 0, hi=1000;
    int ans = 0;
    while (lo <= hi) {
        int mid = lo + (hi - lo)/2;
        if (checkHIndex(citations, mid)) {
            ans = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return ans;
}

int main() {
    vector<int> test1 = vector<int>({3,0,6,1,5});
    cout << hIndex(test1);

}

