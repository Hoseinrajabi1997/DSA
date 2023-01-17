def lcs(s1, s2):
    i, j = 0, 0
    track = [[-1 for i in range(len(s2))] for j in range(len(s1))]
    return lcs_rec(s1, s2, i, j, track)


def lcs_rec(s1, s2, i, j, track):
    if i == len(s1) or j == len(s2):
        return 0

    if track[i][j] != -1:
        return track[i][j]

    if s1[i] == s2[j]:
        track[i][j] = 1 + lcs_rec(s1, s2, i + 1, j + 1, track)
    else:
        track[i][j] = max(lcs_rec(s1, s2, i + 1, j, track), lcs_rec(s1, s2, i, j + 1, track))

    return track[i][j]


if __name__ == '__main__':
    s1 = "PythonRocks"
    s2 = "PythonIsFun"
    print(" LCS = ", lcs(s1, s2))