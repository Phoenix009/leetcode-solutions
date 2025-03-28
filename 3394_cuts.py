def solve(n, rectangles):
    def count_overlaps(intervals):
        count = 1
        left, right = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < right:
                right = max(right, intervals[i][1])
            else:
                count += 1
                left, right = intervals[i]
        print(count)
        return count

    y_intervals = []
    x_intervals = []
    for a, b, x, y in rectangles:
        y_intervals.append((b, y))
        x_intervals.append((a, x))

    x_intervals.sort()
    y_intervals.sort()

    if count_overlaps(y_intervals) >= 3:
        return True
    if count_overlaps(x_intervals) >= 3:
        return True
    return False


print(solve(5, [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]))
print(solve(4, [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]))
print(solve(4, [[0, 2, 2, 4], [1, 0, 3, 2], [
      2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]))
