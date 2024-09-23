def maximumOddBinaryNumber(s: str) -> str:
    count1 = s.count('1') - 1
    res = ['0'] * len(s)
    res[-1] = '1'
    for i in range(count1):
        res[i] = '1'
    return ''.join(res)

print(maximumOddBinaryNumber("010"))
print(maximumOddBinaryNumber("0101"))

