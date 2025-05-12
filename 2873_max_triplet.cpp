#include <iostream>

using namespace std;

long long solve(vector<int> nums) {
    long long ans = 0;
    
    for (int i=0; i<nums.size(); i++) {
        for (int j=i+1; j<nums.size(); j++) {
            for (int k=j+1; k<nums.size(); k++) {
                long long acc = (nums[i] - nums[j]) * nums[k];
                ans = max(ans, acc);
            }
        }
    }

    return ans;
}

int main() {
    cout << solve({12, 6, 1, 2, 7}) << endl;
    cout << solve({7, 10, 3, 4, 19}) << endl;
    cout << solve({1, 2, 3}) << endl;
}


