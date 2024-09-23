def flipAndInvertImage(image):
    res = []
    for row in image:
        row = row[::-1]
        row = [0 if i == 1 else 1 for i in row]
        res.append(row)
    return res
