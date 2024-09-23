def construct2DArray(original, m: int, n: int):
    def get_rows(arr, length):
        for i in range(0, len(arr), length):
            yield arr[i:i+length]

    return [row for row in get_rows(original, m)]
    



print(construct2DArray([1,2], 1, 1))
