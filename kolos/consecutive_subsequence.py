# Mając na wejściu tablicę liczb naturalnych znaleźć długość najdłuższego podciągu kolejnych liczb
# naturalnych. Algorytm powinien działać w czasie O(n). Przykład: [1,5,3,4,8,10,12,11], odpowiedzią jest 3.
# Ciągiem może być 3,4,5 lub 10,11,12


def longest_subsequence(arr):
    dictionary = set(arr)
    result = 0
    for i in arr:
        if i - 1 not in dictionary:
            j = i
            while j in dictionary:
                j += 1
                result = max(result, j - i)
    return result


print(longest_subsequence([1,5,3,4,8,10,12,11]))
