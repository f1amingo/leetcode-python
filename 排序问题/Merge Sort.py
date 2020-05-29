def merge(a, tmp, low, mid, high):
    i, j, pos = low, mid + 1, low
    while i <= mid and j <= high:
        # 等于，稳定性保证
        if a[i] <= a[j]:
            tmp[pos] = a[i]
            i += 1
        else:
            tmp[pos] = a[j]
            j += 1
        pos += 1
    for k in range(i, mid + 1):
        tmp[pos] = a[k]
        pos += 1
    for k in range(j, high + 1):
        tmp[pos] = a[k]
        pos += 1
    a[low:high + 1] = tmp[low:high + 1]


# [low, high]
def mergeSort(a, tmp, low, high):
    # 注意判断条件，这里要确保有两个元素，一个元素时即可跳出
    if low < high:
        mid = (low + high) // 2
        mergeSort(a, tmp, low, mid)
        mergeSort(a, tmp, mid + 1, high)
        # 优化
        if a[mid] <= a[mid + 1]:
            return
        merge(a, tmp, low, mid, high)


arr = [-2, 3, -5]
tmp = [0] * len(arr)
mergeSort(arr, tmp, 0, len(arr) - 1)
print(arr)
