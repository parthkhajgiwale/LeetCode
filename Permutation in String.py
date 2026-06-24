def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    def idx(c):
        return ord(c) - ord('a')

    count_s1 = [0] * 26
    window = [0] * 26

    for ch in s1:
        count_s1[idx(ch)] += 1

    for i in range(len(s1)):
        window[idx(s2[i])] += 1

    if window == count_s1:
        return True

    for i in range(len(s1), len(s2)):
        window[idx(s2[i])] += 1
        window[idx(s2[i - len(s1)])] -= 1

        if window == count_s1:
            return True

    return False
