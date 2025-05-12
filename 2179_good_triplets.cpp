#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>

using namespace std;

long long solve(vector<int> nums1, vector<int> nums2) {

    long long ans = 0;

    // for each int it stores the set of values that have occured before it
    unordered_map<int, set<int>> store1{};
    set<int> store{};

    for (auto item: nums1) {
        store1[item] = store;
        store.insert(item);
    }

    // for (auto nums: store1) {
    //     cout << nums.first << ": ";
    //     for (auto item: nums.second) cout << item << " ";
    //     cout << endl;
    // }
    
    set<int> super{};
    for(int i=0; i<nums1.size(); i++) super.insert(i);

    store.clear();
    for (auto item: nums2) {
        // cout << item << ": " << endl;

        set<int> before{};
        set_intersection(
            store.begin(), store.end(),
            store1[item].begin(), store1[item].end(),
            inserter(before, before.begin())
        );
        int count_before = before.size();


        
        store.insert(item);
        set<int> after1{};
        set_difference(
            super.begin(), super.end(),
            store.begin(), store.end(),
            inserter(after1, after1.begin())
        );

        store1[item].insert(item);
        set<int> after2{};
        set_difference(
            super.begin(), super.end(),
            store1[item].begin(), store1[item].end(),
            inserter(after2, after2.begin())
        );

        set<int> after{};
        set_intersection(
            after1.begin(), after1.end(),
            after2.begin(), after2.end(),
            inserter(after, after.begin())
        );
        int count_after = after.size();

        
        ans += 1ll * count_before * count_after;

        // for (auto item: before) cout << item << " ";
        // cout << endl;
        // for (auto item: after) cout << item << " ";
        // cout << endl << endl;
    }

    return ans;
}

int main() {
    cout << solve({2, 0, 1, 3}, {0, 1, 2, 3}) << endl;
    cout << solve({4, 0, 1, 3, 2}, {4, 1, 0, 2, 3}) << endl;
}
