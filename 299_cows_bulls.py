def solve(secret, guess):
    from collections import defaultdict
    
    frq_secret = defaultdict(int)
    frq_guess = defaultdict(int)

    # bulls:
    bulls = 0
    for alpha_secret, alpha_guess in zip(secret, guess):
        if alpha_secret == alpha_guess:
            bulls += 1
        else:
            frq_secret[alpha_secret] += 1
            frq_guess[alpha_secret] += 1

    # cows:
    cows = 0
    for key in frq_guess:
        cows += min(frq_guess[key], frq_secret[key])

    return f"{bulls}A{cows}B"


