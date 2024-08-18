def quicksort(array):
    """Быстрая сортировка."""
    len_array = len(array)

    # Базовый случай рекурсии.
    if len_array <= 1:
        return array
    # Определяем индекс опорного элемента и получаем сам опорный элемент:
    middle_element_index = len_array // 2
    pivot = array[middle_element_index]

    # Передаём в функцию partition() массив и опорный элемент;
    # partition() вернёт кортеж с тремя списками;
    # распаковываем этот кортеж в три переменные.
    left, center, right = partition(array, pivot)
    # Для каждой части массива рекурсивно вызываем функцию quicksort().
    ...


def partition(array, pivot):
    """
    Разбивает массив на три разных массива относительно опорного элемента.
    """
    # Создаём три пустых списка.
    left, center, right = [], [], []
    # Раскладываем элементы по спискам.
    for item in array:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            center.append(item)
    # Возвращаем кортеж с тремя списками.
    return left, center, right
