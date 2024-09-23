def isRectangleOverlap(rec1, rec2) -> bool:
    if rec1[0] == rec2[0] or rec1[1] == rec2[1]:
        return True
    if rec1[0][0] < rec2[0][0] < rec1[1][0] or \
        rec1[0][0] < rec2[1][0] < rec1[1][0] or \
        rec1[0][1] < rec2[0][1] < rec1[1][1] or \
        rec1[0][1] < rec2[1][1] < rec1[1][1]:
        return True
    return False
