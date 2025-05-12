#include <functional>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

long long solve(vector<int> weights, int k) {
    long long maxi = weights[0] + weights[weights.size() - 1];

    priority_queue<int> heap {};
    for (int i=1; i<weights.size(); i++) {
        heap.push(weights[i] + weights[i-1]);
    }

    for (int i=1; i<k; i++) {
        std::cout << heap.top() << std::endl;
        maxi += heap.top();
        heap.pop();
    }

    long long mini = weights[0] + weights[weights.size() - 1];
    
    priority_queue<int, vector<int>, greater<int>> min_heap{};

    for (int i=1; i<weights.size(); i++) {
        min_heap.push(weights[i] + weights[i-1]);
    }

    for (int i=1; i<k; i++) {
        mini += min_heap.top();
        min_heap.pop();
    }
    
    return maxi - mini;
}

int main() {
    cout << solve({1, 3, 5, 1}, 2) << endl;
    cout << solve({1, 3}, 2) << endl;
}
