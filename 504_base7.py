def solution(num):
    is_negative = num < 0
    res = ""

    if is_negative:
        num *= -1

    while (num):
        res = str(num % 7) + res
        num //= 7

    if is_negative:
        res = "-" + res
    return res


print(solution(100))
print(solution(-7))

