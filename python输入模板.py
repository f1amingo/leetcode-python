while True:
    try:
        x_list = input().split()
        if x_list[0] == '0' and x_list[1] == '0':
            break
        print(int(x_list[0]) + int(x_list[1]))
    except EOFError:
        break
