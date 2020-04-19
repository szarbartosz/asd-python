# naive recursion
def lcs_recursive(str1, str2, i1, i2):
    if i1 == len(str1) or i2 == len(str2):
        return 0
    elif str1[i1] == str2[i2]:
        return 1 + lcs_recursive(str1, str2, i1 + 1, i2 + 1)
    else:
        return max(lcs_recursive(str1, str2, i1 + 1, i2), lcs_recursive(str1, str2, i1, i2 + 1))


# str1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'B', 'L', 'K', 'Z', 'O', 'J']
# str2 = ['R', 'B', 'N', 'D', 'S', 'E', 'F', 'H', 'M', 'G', 'L', 'Z', 'K', 'J', 'W']
# print(lcs_recursive(str1, str2, 0, 0))


# dp with memoising
def lcs_memo_wrap(str1, str2):
    memo = [None] * (len(str1) + 1)
    for i in range(len(str1) + 1):
        memo[i] = [None] * (len(str2) + 1)
    return lcs_memo(str1, str2, 0, 0, memo)


def lcs_memo(str1, str2, i1, i2, memo):
    if memo[i1][i2] is not None:
        return memo[i1][i2]
    if i1 == len(str1) or i2 == len(str2):
        result = 0
    elif str1[i1] == str2[i2]:
        result = 1 + lcs_memo(str1, str2, i1 + 1, i2 + 1, memo)
    else:
        result = max(lcs_memo(str1, str2, i1 + 1, i2, memo), lcs_memo(str1, str2, i1, i2 + 1, memo))
    memo[i1][i2] = result
    return result


# str1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'B', 'L', 'K', 'Z', 'O', 'J']
# str2 = ['R', 'B', 'N', 'D', 'S', 'E', 'F', 'H', 'M', 'G', 'L', 'Z', 'K', 'J', 'W']
# print(lcs_memo_wrap(str1, str2))


# iterative
def lcs_iterative(str1, str2):
    memo = [None] * (len(str1) + 1)
    for i in range(len(str1) + 1):
        memo[i] = [None] * (len(str2) + 1)
    for i in range(len(str2) + 1):
        memo[len(str1)][i] = 0
    for i in range(len(str1) + 1):
        memo[i][len(str2)] = 0
    for i in range(len(str1) - 1, -1, -1):
        for j in range(len(str2) - 1, -1, -1):
            if str1[i] == str2[j]:
                memo[i][j] = 1 + memo[i + 1][j + 1]
            else:
                memo[i][j] = max(memo[i + 1][j], memo[i][j + 1])
    return memo[0][0]


str1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'B', 'L', 'K', 'Z', 'O', 'J']
str2 = ['R', 'B', 'N', 'D', 'S', 'E', 'F', 'H', 'M', 'G', 'L', 'Z', 'K', 'J', 'W']
print(lcs_iterative(str1, str2))
