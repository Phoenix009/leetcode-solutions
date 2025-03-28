def removeOccurrences(s: str, part: str) -> str:
    stack = ""
    for alpha in s:
        stack += alpha

        if len(stack) >= len(part) and stack[-len(part):] == part:
            stack = stack[: -len(part)]

    return stack

print(removeOccurrences("daabcbaabcbc", "abc"))
print(removeOccurrences("axxxxyyyyb", "xy"))


