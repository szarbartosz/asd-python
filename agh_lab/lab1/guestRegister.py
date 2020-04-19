#Consider a big party where a log register for guest’s entry and exit times is maintained.
#Find the time at which there are maximum guests in the party. Note that entries in register are not in any order.
#INPUT: First line No of Intervals. Then Entry array and exit array
#OUTPUT: Max no of guests and time interval

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def func(entry, exit):
    entry = selectionSort(entry)
    exit = selectionSort(exit)
    beg = None
    end = None
    inside = 0
    max_guest = 0
    j = 0
    for i in range(len(entry)):
        if entry[i] < exit[j]:
            inside += 1
            if inside > max_guest:
                max_guest = inside
                beg = entry[i]
        elif entry[i] > exit[j]:
            inside -= 1
            j += 1
            end = exit[j]
        else:
            j += 1
    return max_guest, beg, end

if __name__=='__main__':
    entry = [1,2,9,5,5]
    exit = [4,5,12,9,12]
    a, b, c = func(entry,exit)
    print("There were maximum", a, "guest(s)", "between", b, "and", c)

