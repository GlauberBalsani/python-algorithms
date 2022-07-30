


def selectionSort(arr):
    minor  = arr[0]
    for i in range(len(arr)):
        if arr[i] <  minor:
            minor = arr[i]
    return minor


print(selectionSort([3, 5, 7, 10, 0, 2]))


