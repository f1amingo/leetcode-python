# [i, j)
def partition(a, i, j):
    p = a[i]
    m = i
    for k in range(i + 1, j):
        if a[k] < p:
            m += 1
            a[m], a[k] = a[k], a[m]
    a[i], a[m] = a[m], a[i]
    return m


# [low, high)
def quick_sort(a, low, high):
    # 判断 km
    if low < high:
        m = partition(a, low, high)
        quick_sort(a, low, m)
        quick_sort(a, m + 1, high)


a = [27, 38, 12, 39, 27, 16]
quick_sort(a, 0, len(a))
print(a)
