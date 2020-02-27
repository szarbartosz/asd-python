#binarySearch - O(log(n))
def binarySearch(sortedArr, beg, end, key):
    if end >= beg:
        mid = (beg + end) // 2
        if sortedArr[mid] == key:
            print("element:", sortedArr[mid], "found at index:", mid)
            return mid
        elif key > sortedArr[mid]:
            return binarySearch(sortedArr, mid + 1, end, key)
        else:
            return binarySearch(sortedArr, beg, mid - 1, key)
    else:
        print("element", key, "not found")
        return None

arr = [1,2,3,4,5,6,7,8,9]
binarySearch(arr, 0, len(arr)-1, 8)