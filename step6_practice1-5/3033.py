while True:
    try:
        have_list = list(map(int, input().split()))
        chess = [1, 1, 2, 2, 2, 8]

        for i in range(len(have_list)):
            print(have_list[i] - chess[i], end='')

    except EOFError:
        break
