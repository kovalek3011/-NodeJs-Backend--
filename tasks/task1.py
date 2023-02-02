def city(city_list: list) -> str:
    return f"{', '.join(city_list)}."


s = ['Москва', 'Санкт-Петербург', 'Воронеж']
# s = input().split()

print(city(s))

# время выполнения 5 мин
