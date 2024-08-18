# В аргумент key будем передавать не функцию, а индекс того элемента кортежа,
# который будет ключом сортировки.
def insertion_sort_by_key(arr, key):
    for i in range(1, len(arr)):
        current = arr[i]
        prev = i - 1
        # Вместо вызова функции указываем нужный элемент кортежа.
        while prev >= 0 and arr[prev][key] > current[key]:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = current


cards = [
    (2, 'Белый'),
    (9, 'Серо-голубой'),
    (11, 'Коралловый'),
    (7, 'Зелёный'),
    (1, 'Чёрный')
]
# Сортируем по названию цвета (по второму элементу кортежа):
insertion_sort_by_key(cards, 1)
print('По цвету:', cards)

# Сортируем по числу на карте (по первому элементу кортежа):
insertion_sort_by_key(cards, 0)
print('По числу:', cards)
