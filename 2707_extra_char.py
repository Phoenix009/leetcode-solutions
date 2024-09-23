def minExtraChar(s, dictionary):
    dp = [0] +  [float('inf') for i in range(len(s))]
    for right_index in range(1, len(s) + 1):
        for left_index in range(1, right_index+1):
            current_word = s[left_index - 1:right_index]
            if current_word in dictionary:
                dp[right_index] = min(
                    dp[right_index],
                    dp[left_index - 1]
                )
        dp[right_index] = min(dp[right_index - 1] + 1, dp[right_index])
    return dp[-1]




print(minExtraChar("leetscode", {"leet","code","leetcode"}))
print(minExtraChar("sayhelloworld", {"hello","world"}))

