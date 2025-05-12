#include <iostream>
#include <unordered_map>

using namespace std;

long long solve(vector<int> nums, int modulo, int k)
{
    unordered_map<int, int> frq;
    long long ans = 0;
    int current_sum = 0;

    frq[0] = 1;

    for (auto num : nums)
    {
        current_sum += num % modulo == k;
        ans += frq[(current_sum - k + modulo) % modulo];
        frq[current_sum % modulo]++;
    }
    return ans;
}

int main()
{
    cout << solve({3, 2, 4}, 2, 1) << endl;
    cout << solve({3, 1, 9, 6}, 3, 0) << endl;
}
