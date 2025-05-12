#include <iostream>
#include <limits>

using namespace std;

int solve(vector<int> nums) {
    if (nums.size() == 1) return 0;

    int ans = 0;
    bool flg = true;
    for (int i=1; i<nums.size(); i++) {
        if (nums[i] < nums[i-1]) {
            flg = false;
            break;
        }    
    }

    while (!flg) {
        ans++;
        int mini_sum = nums[0] + nums[1];
        int min_index1 = 1;
        for (int i=2; i<nums.size(); i++) {
            if (nums[i] + nums[i-1] < mini_sum) {
                mini_sum = nums[i] + nums[i-1];
                min_index1 = i;
            }
        }
        nums.erase(nums.begin() + min_index1 - 1, nums.begin() + min_index1 + 1); // removes elements at i-1 and i
        nums.insert(nums.begin() + min_index1 - 1, mini_sum); 

        // for (auto item: nums) cout << item << " ";
        // cout << endl;

        flg = true;
        for (int i=1; i<nums.size(); i++) {
            if (nums[i] < nums[i-1]) {
                flg = false;
                break;
            }    
        }
    }
    return ans;
}

int main() {
    cout << solve({5, 2, 3, 1}) << endl;
    cout << endl;
    cout << solve({1, 2, 2}) << endl;
}
