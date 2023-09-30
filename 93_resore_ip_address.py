# class Solution:
#     def restoreIpAddresses(self, s: str) -> List[str]:
#         pass

def is_valid_octet(part):
    if len(part) == 1: return 0 <= int(part) <= 9
    if len(part) == 2: return 10 <= int(part) <= 99
    if len(part) == 3: return 100 <= int(part) <= 255
    return False


def helper(s, index, part, res):
    if part == 4:
        if is_valid_octet(s[index:]):
            yield f"{res}{s[index:]}"
    else:
        octet = ""
        for i in range(3):
            if index + i >= len(s): break

            octet += s[index + i]
            if is_valid_octet(octet):
                yield from helper(s, index + i + 1, part + 1, f"{res}{octet}.")
            else: break

s = "25525511135"
ans = list(helper(s, 0, 1, ""))
print(ans)


