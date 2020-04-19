#QuickSort - O(nlog(n)), pesymistyczna - O(n^2)
def partition(arr, left, right):
    i = (left - 1)
    pivot = arr[right]
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1

def quickSort(arr, left, right):
    if right > left:
        mid = partition(arr, left, right)
        quickSort(arr, left, mid - 1)
        quickSort(arr, mid + 1, right)

if __name__=='__main__':
    arr = [32,53,56,2,3,5,1,4,2,324,45,4576,45,2,3]
    quickSort(arr,0,len(arr)-1)
    print(arr)