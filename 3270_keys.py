
def generateKey(num1: int, num2: int, num3: int) -> int:
    def pad_zeroes(num):
        num = str(num)
        num = "0"*(max(0, 4 - len(num))) + num
        return num

    num1 = pad_zeroes(num1)
    num2 = pad_zeroes(num2)
    num3 = pad_zeroes(num3)

    print(num1, num2, num3)

    res = ""
    for i in range(4):
        res += str(min(int(num1[i]), int(num2[i]), int(num3[i])))
    return int(res)


print(generateKey(10, 100, 1000))


