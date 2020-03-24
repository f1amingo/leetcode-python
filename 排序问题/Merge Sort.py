def merge(a, low, mid, high):
    N = high - low + 1
    b = [0] * N
    left, right, bIdx = low, mid + 1, 0
    while left <= mid and right <= high:
        if a[left] <= a[right]:
            b[bIdx] = a[left]
            left += 1
        else:
            b[bIdx] = a[right]
            right += 1
        bIdx += 1
    while left <= mid:
        b[bIdx] = a[left]
        bIdx += 1
        left += 1
    while right <= high:
        b[bIdx] = a[right]
        bIdx += 1
        right += 1
    for k in range(N):
        a[low + k] = b[k]


def mergeSort(a, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(a, low, mid)
        mergeSort(a, mid + 1, high)
        merge(a, low, mid, high)


arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
mergeSort(arr, 0, len(arr) - 1)
print(arr)
