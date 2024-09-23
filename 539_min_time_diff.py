from functools import cmp_to_key


def findMinDifference(timePoints) -> int:
    def get_value(point):
        (p1, p2) = tuple(map(int, point.split(':')))
        return p1*60 + p2

    values = [get_value(point) for point in timePoints]
    values.sort()

    ans = float('inf')
    for a, b in zip(values, values[1:]):
        ans = min(ans, b - a)

    ans = min(ans, (1440 + values[0]) - values[-1])
    return ans


print(findMinDifference(["23:59", "00:00"]))
