def subsequence(arr1, arr2, i1, i2, memo):
    if memo[i1][i2] is not None:
        return memo[i1][i2]
    if i1 == len(arr1) or i2 == len(arr2):
        result = 0
    elif arr1[i1] == arr2[i2]:
        result = 1 + subsequence(arr1, arr2, i1+1, i2+1, memo)
    else:
        result = max(subsequence(arr1, arr2, i1+1, i2, memo),
                     subsequence(arr1, arr2, i1, i2+1, memo))
    memo[i1][i2] = result
    return result


def subsequence_wrapper(arr1, arr2):
  memo = [None] * (len(arr1) + 1)
  for i in range(len(arr1) + 1):
    memo[i] = [None] * (len(arr2) + 1)
  return subsequence(arr1, arr2, 0, 0, memo)


arr1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
arr2 = ['R', 'B', 'N', 'D', 'S', 'E', 'F', 'H', 'M']
print(subsequence_wrapper(arr1, arr2))