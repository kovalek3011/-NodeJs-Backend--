def rounding(num: float) -> int:
    if num % 10 < 5:
        return int(num // 10 * 10)
    else:
        return int((num // 10 + 1) * 10)


print(rounding(float(input())))

# время выполнения 15 мин
