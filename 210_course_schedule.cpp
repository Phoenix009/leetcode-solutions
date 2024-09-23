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

bool dfs(unordered_map<int, set<int>>& graph, vector<int>& color, int src, vector<int>& answer) {
    color[src] = 1;
     for (auto dst: graph[src]) {
        if (color[dst] == 1) return false;
        if (color[dst] == 2) continue;
        if (!dfs(graph, color, dst, answer))
            return false;
    }
    answer.push_back(src);
    color[src] = 2;
    return true;
}

bool topological_sort(unordered_map<int, set<int>>& graph, int nnodes, vector<int>& answer) {
    vector<int> color = vector<int>(nnodes, 0);
    for (int i=0; i<nnodes; i++) {
        if (color[i] == 2) continue;
        if (!dfs(graph, color, i, answer)) return false;
    }
    return true;
}

vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
    unordered_map<int, set<int>> graph = unordered_map<int, set<int>>();

    for (int i=0; i<numCourses; i++)
        graph[i] = set<int>();

    for(int i=0; i<prerequisites.size(); i++)
        graph[prerequisites[i][1]].insert(prerequisites[i][0]);
    

    vector<int> topological_order = vector<int>();
    bool has_ans = topological_sort(graph, numCourses, topological_order);

    if (has_ans){
        return topological_order;

    }
    else return {};
}

int main() {
    vector<vector<int>> t1= {{1,0},{2,0},{3,1},{3,2}};
    vector<int> ans = findOrder(4, t1);
    for (auto node: ans) cout << node << " ";
    cout << endl;
}
