from sortingAlgorithms import merge_sort

def maxTripletProduct(arr):
    merge_sort.mergeSort(arr)
    neg_count = 0
    pos_count = 0
    res = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > 0:
            pos_count += 1
        elif arr[i] < 0:
            neg_count += 1
    if pos_count >= 1:
        res = max(arr[n-1]*arr[n-2]*arr[n-3], arr[0]*arr[1]*arr[n-1])
    if pos_count == 0:
        res = arr[n-1]*arr[n-2]*arr[n-3]
    return res

if __name__=='__main__':
    arr_pos = [10, 3, 5, 6, 20]
    arr_neg = [-10,-3,-5,-6,-20]
    print(maxTripletProduct(arr_pos))
    print(maxTripletProduct(arr_neg))
