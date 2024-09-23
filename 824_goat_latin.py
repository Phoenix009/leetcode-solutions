def toGoatLatin(sentence: str) -> str:
    res = []
    for index, word in enumerate(sentence.split()):
        if word[0] in "aeiouAEIOU":
            word = word + "ma"
        else:
            word = word[1:] + word[0] + "ma"

        word += "a" * (index+1)
        res.append(word)

    return " ".join(res)



