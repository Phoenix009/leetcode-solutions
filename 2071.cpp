#include <iostream>
#include <queue>
#include <functional>
#include <set>

using namespace std;


int solve(vector<int> tasks, vector<int> workers, int pills, int strength)
{
    sort(begin(tasks), end(tasks));
    sort(begin(workers), end(workers));

    int tasks_completed = 0;
    int used_pills = 0;
    multiset<int> workersFree(workers.begin(), workers.end());

    for(int i = tasks.size() - 1; i >= 0; --i) {
        auto it = prev(workersFree.end());
        bool canAssign = true;

        if(*it < tasks[i]) {
            it = workersFree.lower_bound(tasks[i] - strength);
            if(it == workersFree.end()) canAssign = false;
            
            ++used_pills;
            if(used_pills > pills)  canAssign = false;
        }
        workersFree.erase(it);
        if (canAssign) tasks_completed++;
    }

    return tasks_completed;
}

int main()
{
    cout << solve({3, 2, 1}, {0, 3, 3}, 1, 1) << endl;
    cout << solve({5, 4}, {0, 0, 0}, 1, 5) << endl;
    cout << solve({10, 15, 30}, {0, 10, 10, 10, 10}, 3, 10) << endl;
    cout << solve({5, 9, 8, 5, 9}, {1, 6, 4, 2, 6}, 1, 5) << endl;
}
