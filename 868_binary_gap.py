from time import sleep


def binaryGap(n: int) -> int:
    s = bin(n)[2:]
    ans = 0
    start_index = s.find('1')
    end_index = s[start_index+1:].find('1') + start_index + 1
    while end_index > start_index:
        length = end_index - start_index + 1
        ans = max(ans, length)
        start_index = end_index
        end_index = s[start_index+1:].find('1') + start_index + 1
    return ans


print(binaryGap(33865))

