def generate_happy_strings(n):
    def helper(curr_str, n):
        if len(curr_str) == n: yield curr_str[1:]
        else:

            for alpha in "abc":
                if alpha != curr_str[-1]:
                    yield from helper(curr_str + alpha, n)

    yield from helper("0", n+1)


n = 1
k = 4

it = generate_happy_strings(n)
try:
    while k-1 and next(it):
        k -= 1
    return next(it)
except: return ""
