#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<int> solve(vector<vector<int>> grid, vector<int> queries)
{
    int num_rows = grid.size();
    int num_cols = grid[0].size();
    
    vector<int> ans(queries.size());

    vector<pair<int, int>> queries_idx;
    for (int i = 0; i < queries.size(); i++)
        queries_idx.push_back({queries[i], i});
    sort(queries_idx.begin(), queries_idx.end());

    using T = tuple<int, int, int>; // (value, x, y)
    priority_queue<T, vector<T>, greater<T>> minHeap;

    minHeap.push({grid[0][0], 0, 0});

    vector<vector<bool>> visited(num_rows, vector<bool>(num_cols, false));
    visited[0][0] = true;

    int score = 0;

    for (auto [query, idx] : queries_idx)
    {
        while (!minHeap.empty() && get<0>(minHeap.top()) < query)
        {
            auto [val, x, y] = minHeap.top();
            minHeap.pop();
            score++;

            int dx[4] = {0, -1, 0, 1};
            int dy[4] = {-1, 0, 1, 0};

            for (int d = 0; d < 4; d++)
            {
                int nx = x + dx[d];
                int ny = y + dy[d];

                if (nx < 0 || nx >= num_rows || ny < 0 || ny >= num_cols)
                    continue;
                if (visited[nx][ny])
                    continue;

                visited[nx][ny] = true;
                minHeap.push({grid[nx][ny], nx, ny});
            }
        }
        ans[idx] = score;
    }

    return ans;
}

int main()
{
    vector<int> ans = solve(
        {{1, 2, 3}, {2, 5, 7}, {3, 5, 1}},
        {5, 6, 2});

    for (auto item : ans)
    {
        std::cout << item << " ";
    }
    std::cout << std::endl;

    ans = solve(
        {{5, 2, 1}, {1, 1, 2}},
        {3});

    for (auto item : ans)
    {
        std::cout << item << " ";
    }
    std::cout << std::endl;

    return 0;
}
