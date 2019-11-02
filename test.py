def foo():
    integer = 1
    arr = []

    def bar():
        arr.append(1)
        print(integer)
        print(arr)

    bar()


n = 3
list1 = [[0] * n] * n
list2 = [[0] * n for _ in range(n)]
list1[0][0] = True
list2[0][0] = True
print(list1)
print(list2)
