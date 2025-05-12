#include <iostream>

using namespace std;

long long solve(vector<int> nums, int k) {
    long long invalid_subarr = 0;

    unordered_map<int, int> frq{};
    int count_pairs = 0;
    int left = 0, right = 0;

    while (left < nums.size()) {
        // expand right while the subarr is not good
        while (right < nums.size() && count_pairs < k) {
            count_pairs += frq[nums[right]];
            frq[nums[right]]++;
            right++;
        }

        right--;

        if (count_pairs >= k) {
            count_pairs -= frq[nums[right]];
            frq[nums[right]]--;
            right--;
        }
        
        int length = right - left + 1;
        invalid_subarr += length;
    
        cout << left << " " << right << endl;

        // Remove the left element and move to the next
        count_pairs -= frq[nums[left]];
        frq[nums[left]]--;
        left++;

    }

    int length = nums.size();
    long long total_subarr = length * (length - 1);
    cout << total_subarr << " - " << invalid_subarr << ": " << total_subarr - invalid_subarr << endl;
    return 0ll;
}

int main() {
    cout << solve({1, 1, 1, 1, 1}, 10) << endl;
    cout << solve({3, 1, 4, 3, 2, 2, 4}, 2) << endl;
}
