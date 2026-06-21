def characterReplacement(s, k):

    count = {}
    left = 0
    maxFreq = 0
    answer = 0

    for right in range(len(s)):

        # Add current character to the window
        count[s[right]] = count.get(s[right], 0) + 1

        # Update highest frequency seen so far
        maxFreq = max(maxFreq, count[s[right]])

        # If window is invalid, shrink it
        while (right - left + 1) - maxFreq > k:

            count[s[left]] -= 1
            left += 1

        # Update longest valid window
        answer = max(answer, right - left + 1)

    return answer
s = "XYYXX"
k = 2
print(characterReplacement(s,k))
