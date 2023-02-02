def multiplication_table(num: int) -> print:
    s = [[i for i in range(num + 1)] for _ in range(num + 1)]

    for i in range(num + 1):
        for j in range(num + 1):
            s[i][j] = i * j

    for i in range(num + 1):
        s[0][i] = i
        s[i][0] = i

    s[0][0] = ''

    for r in range(num + 1):
        for c in range(num + 1):
            print(str(s[r][c]).rjust(2), end=' ')
        print()


multiplication_table(int(input()))

# время выполнения 35 мин
