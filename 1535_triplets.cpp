#include <iostream>

using namespace std;

int solve(vector<int> nums, int a, int b, int c) {
    int count = 0;
    
    vector<vector<int>> jss {};
    vector<vector<int>> kss {};
        
    for (int i=0; i<nums.size(); i++) {
        vector<int> js {};
        vector<int> ks {};

        for (int j=i+1; j<nums.size(); j++) {
            if (abs(nums[i] - nums[j]) <= a) js.push_back(j);
            if (abs(nums[i] - nums[j]) <= c) ks.push_back(j);
        }

        jss.push_back(js);
        kss.push_back(ks);
    }

    for (int i=0; i<nums.size(); i++) {
        for (auto j: jss[i]) {
            for (auto k: kss[i]) {
                if (k > j) continue;
                if (abs(nums[j] - nums[k]) <= b) count++;
            }
        }
    }

    return count;
}

int main() {
    cout << solve({3,0,1,1,9,7}, 7, 2, 3) << endl;
    cout << solve({1,1,2,2,3}, 0, 0, 1) << endl;
}
