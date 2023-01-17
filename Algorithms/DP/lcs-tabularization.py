def lcs(s1, s2):

    track = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 or j == 0:
                track[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                track[i][j] = 1 + track[i-1][j-1]
            else:
                track[i][j] = max(track[i-1][j], track[i][j-1])
    print(track)
    return track[len(s1)][len(s2)]



if __name__ == '__main__':
    s1 = "PythonRocks"
    s2 = "PythonIsFun"
    print(" LCS = ", lcs(s1, s2))