def change_case(num: int) -> str:
    if num % 10 == 1 and num % 100 != 11 and num != 11:
        return f'{num} компьютер'
    elif num % 10 in [2, 3, 4]:
        if num % 100 not in [12, 13, 14]:
            return f'{num} компьютера'
        else:
            return f'{num} компьютеров'
    else:
        return f'{num} компьютеров'


print(change_case(int(input())))

# время выполнения 30 мин
