#include <iostream>
#include <queue>

using namespace std;

bool complete_k_tasks(vector<int>& tasks, vector<int>& workers, int k, int pills, int strength) {
    int tasks_completed = 0;
    int worker_index = 0;

    for (int task_index = 0; task_index < k; task_index++) {
        if (tasks[task_index] <= workers[worker_index]) {
            tasks_completed++;
            task_index++;
            worker_index++;
        } else if (pills && tasks[task_index] <= workers[worker_index] + strength) {
            tasks_completed++;
            task_index++;
            worker_index++;
            pills--;
        } else {
            worker_index++;
        }
    }

    return tasks_completed == k;
}

int solve(vector<int> tasks, vector<int> workers, int pill, int strength) {
    // assume pills are not present
    // to maximise the amount of tasks that are done
    // we want to assign workers task with highest possible difficulty
    
    sort(begin(tasks), end(tasks));
    sort(begin(workers), end(workers));

    int tasks_completed = 0;
    int left = 0, right = tasks.size();
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (complete_k_tasks(tasks, workers, mid, pill, strength)) {
            tasks_completed = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return tasks_completed;
}

int main() {
    cout << solve({3, 2, 1}, {0, 3, 3}, 1, 1) << endl;
    cout << solve({5, 4}, {0, 0, 0}, 1, 5) << endl;
    cout << solve({10, 15, 30}, {0, 10, 10, 10, 10}, 3, 10) << endl;
}
