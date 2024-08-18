def list_superset(list_set_1, list_set_2):
    # Не меняйте названия функции и параметров. Напишите решение здесь.
    if len(list_set_1) >= len(list_set_2):
        return superset_check(list_set_1, list_set_2)
    else:
        return superset_check(list_set_2, list_set_1)


def superset_check(list_superset, list_set):
    index = 0
    for element in list_set:
        if element in list_superset:
            index += 1

    if len(list_set) == index and len(list_superset) == index:
        return 'Наборы равны.'
    elif len(list_set) == index and len(list_superset) > index:
        return f'Набор {list_superset} - супермножество.'
    else:
        return 'Супермножество не обнаружено.'


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
