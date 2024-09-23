def largeGroupPositions(s: str):
    res = []
    start_index = 0
    end_index = 0
    while (start_index < len(s)):
        while (end_index < len(s) and s[end_index] == s[start_index]):
            end_index += 1
        
        current_length = end_index - start_index
        if current_length > 2:
            res.append([start_index, end_index - 1])
        start_index = end_index
    return res


print(largeGroupPositions("abcdddeeeeaabbbcd"))
