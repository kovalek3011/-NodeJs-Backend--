def coincidences(list1: list, list2: list) -> list:
    s = []
    for i in list1:
        if i not in s:
            if list1.count(i) >= 2 and list2.count(i) >= 2:
                s.append(i)
    return s


l1, l2 = [7, 17, 1, 9, 1, 17, 56, 56, 23], [56, 17, 17, 1, 23, 34, 23, 1, 8, 1]
# l1, l2 = ([int(i) for i in input().split()] for _ in range(2))
print(coincidences(l1, l2))

# время выполнения 20 мин
