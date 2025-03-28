#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <deque>

using namespace std;

#define max_rows 1000
#define max_cols 1000

int get_score(int query, vector<vector<int>> &grid) {
    bool visited[max_rows][max_cols]  = {false};

    int score = 0;
    
    int num_rows = grid.size();
    int num_cols = grid[0].size();

    deque<pair<int, int>> queue = {{0, 0}};
    visited[0][0] = true;

    while (queue.size()) {
        pair<int, int> current = queue.front();
        int x = current.first, y = current.second;
        queue.pop_front();
        
        if (grid[x][y] >= query) continue;
        
        score++;

        int x_[4] = {0, -1, 0, 1};
        int y_[4] = {-1, 0, 1, -1};
        for (int i=0; i<4; i++) {
            int new_x = x + x_[i];
            int new_y = y + y_[i];
            
            if (new_x < 0 || new_x >= num_rows || new_y < 0 || new_y >= num_cols)
                continue;
            
            if (visited[new_x][new_y]) continue;

            visited[new_x][new_y] = true;
            queue.push_back({new_x, new_y});
        }
    }
    
    return score;
}

vector<int> solve(vector<vector<int>> grid, vector<int> queries) {
    set<int> store_set = set<int>();
    for (auto row: grid) 
        store_set.insert(row.begin(), row.end());

    vector<int> store = vector<int>(store_set.begin(), store_set.end());
    int maxi = *max_element(store.begin(), store.end());
    store.push_back(maxi+1);
    
    vector<int> scores = vector<int>();

    for (auto item: store) {
        scores.push_back(get_score(item, grid));
    }

    for (int i=0; i<scores.size(); i++) {
        std::cout << store[i] << ": " << scores[i] << std::endl;
    }

    vector<int> ans{};

    for (auto query: queries) {
        auto it = upper_bound(store.begin(), store.end(), query);
        if (it == store.begin()) {
            cout<<"At store begin for " << query << endl;
            ans.push_back(0);
        }
        else {
            int n = it - store.begin();
            n--;
            cout << "At " << n << endl;


            ans.push_back(scores[n]);
        }
    }

    return ans;
}

int main() {
    vector<int> ans = solve(
        {{1,2,3},{2,5,7},{3,5,1}},
        {5,6,2}
    );

    for (auto item: ans) {
        std::cout << item << " ";
    }
    std::cout << std::endl;

    

    //
    // ans = solve(
    //     {{5,2,1},{1,1,2}},
    //     {3}
    // );
    //
    // for (auto item: ans) {
    //     std::cout << item << " ";
    // }
    // std::cout << std::endl;
    
    return 0;
}




