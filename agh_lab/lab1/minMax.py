import sys

def func(arr):
    min_val = sys.maxsize
    max_val = -sys.maxsize -1
    if len(arr) % 2 == 0:
        for i in range(0, len(arr), 2):
            if arr[i] > arr[i+1]:
                if arr[i] > max_val:
                    max_val = arr[i]
                if arr[i+1] < min_val:
                    min_val = arr[i+1]
            else:
                if arr[i] < min_val:
                    min_val = arr[i]
                if arr[i+1] > max_val:
                    max_val = arr[i+1]
        return min_val, max_val
    elif len(arr) == 1:
        return arr[0], arr[0]
    else:
        for i in range(0, len(arr) - 1, 2):
            if arr[i] > arr[i+1]:
                if arr[i] > max_val:
                    max_val = arr[i]
                if arr[i+1] < min_val:
                    min_val = arr[i+1]
            else:
                if arr[i] < min_val:
                    min_val = arr[i]
                if arr[i+1] > max_val:
                    max_val = arr[i+1]
        if arr[len(arr)-1] > max_val:
            max_val = arr[len(arr)-1]
        elif arr[len(arr)-1] < min_val:
            min_val = arr[len(arr)-1]
        return min_val, max_val


if __name__=='__main__':
    arr = [3,53,6,13,43,7645,2,34,1,45,645,2,1,32]
    print(func(arr))
