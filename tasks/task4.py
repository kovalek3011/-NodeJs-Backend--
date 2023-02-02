def simple_number(num: int) -> str:
    count = 0
    for i in range(1, num + 1):
        if int(num / i) == num / i:
            count += 1
            if count > 2:
                break
    return 'Число является простым' if count == 2 else 'Число не является простым'


print(simple_number(int(input())))

# время выполнения 25 мин
