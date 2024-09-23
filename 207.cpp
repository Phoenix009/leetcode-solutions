#include <iostream>
#include <unordered_map>
#include <set>

using namespace std;


void printGraph(unordered_map<int, set<int>> graph) {
    for(auto entry: graph) {
        cout << entry.first << ": ";
        for (auto node: entry.second) 
            cout << node << ", ";
        cout << endl;
    }
}

bool dfs(unordered_map<int, set<int>>& graph, vector<int>& color, int src) {
    color[src] = 1;
     for (auto dst: graph[src]) {
        if (color[dst] == 1) return true;
        if (color[dst] == 2) continue;
        if (dfs(graph, color, dst))
            return true;
    }
    color[src] = 2;
    return false;
}

bool hasCycles(unordered_map<int, set<int>>& graph, int nnodes) {
    vector<int> color = vector<int>(nnodes, 0);
    for (int i=0; i<nnodes; i++) {
        if (color[i] == 2) continue;
        if (dfs(graph, color, i)) return true;
    }
    return false;
}

bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
    unordered_map<int, set<int>> graph = unordered_map<int, set<int>>();

    for (int i=0; i<numCourses; i++)
        graph[i] = set<int>();

    for(int i=0; i<prerequisites.size(); i++)
        graph[prerequisites[i][1]].insert(prerequisites[i][0]);
    

    return !hasCycles(graph, numCourses);
}

int main() {
    vector<vector<int>> t1= {{1, 0}};
    cout << canFinish(2, t1) << endl;
}
