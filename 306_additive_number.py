def solve(num):
    if not num: return False
    if num[0] == '0':
        return helper(0, num[1:])

    for i in range(1, len(num)):
        first = int(num[:i])
        if helper(first, num[i:]):
            return True
    return False


def helper(first, num):
    if num[0] == '0':
        return helper1(first, 0, num[1:])

    for i in range(1, len(num)):
        second = int(num[:i])
        if helper1(first, second, num[i:]):
            return True
    return False


def helper1(first, second, num):
    print(first, second)
    if not num:
        return True

    if num[0] == '0':
        if first + second == 0: return helper1(second, 0, num[1:])
        return False


    target = first + second
    if target == int(num[:len(str(target))]):
        return helper1(second, target, num[len(str(target)):])


solve("112358")
