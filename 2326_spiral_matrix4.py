def spiralMatrix(m, n, head):
    res = [[-1 for j in range(n)] for i in range(m)]
    x_ = [0, 1, 0, -1]
    y_ = [1, 0, -1, 0]
    d = 0

    x, y = 0, 0
    for val in head:
        res[x][y] = val

        new_x, new_y = x + x_[d], y+y_[d]
        if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or res[new_x][new_y] != -1:
            d = (d+1) % 4
        x, y = x + x_[d], y+y_[d]

    return res

print(spiralMatrix(3, 5, [3,0,2,6,8,1,7,9,4,2,5,5,0]))
print(spiralMatrix(1, 4, [0, 1, 2]))

