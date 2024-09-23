def convertDateToBinary(date: str) -> str:
    return '-'.join(map(lambda part: bin(int(part))[2:], date.split('-')))

