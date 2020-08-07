# [i, j)
# def partition(a, i, j):
#     p = a[i]  # pivot的值
#     m = i  # 为pivot最终应该在的位置
#     for k in range(i + 1, j):
#         # 碰到一个小于pivot的数
#         if a[k] < p:
#             # pivot的最终位置往右移一位
#             m += 1
#             # 把这个小的数换到左边
#             a[m], a[k] = a[k], a[m]
#     a[i], a[m] = a[m], a[i]
#     return m


# [low, high)
import random


def quick_sort(a, low, high):
    # 判断 km
    if low < high:
        m = partition(a, low, high)
        quick_sort(a, low, m)
        quick_sort(a, m + 1, high)


a = [27, 38, 12, 39, 27, 16]
quick_sort(a, 0, len(a))
print(a)


# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

def partition(arr, low, high):
    # [low, high]
    random_index = random.randint(low, high)
    arr[random_index], arr[low] = arr[low], arr[random_index]
    pivot = arr[low]
    lt = low + 1
    rt = high
    while True:
        while lt <= rt and arr[lt] < pivot:
            lt += 1
        while lt <= rt and arr[rt] > pivot:
            rt -= 1
        if lt > rt:
            break
        arr[lt], arr[rt] = arr[rt], arr[lt]
        lt += 1
        rt -= 1
    arr[low], arr[rt] = arr[rt], arr[low]
    return rt
