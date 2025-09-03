def partition(arr, low, high):
    x = arr[low]  # Опорный элемент (первый элемент подмассива)
    i = low + 1   # Начинаем с элемента после опорного
    for j in range(low + 1, high + 1):  # Проходим с элемента после опорного
        if arr[j] < x:  # Если текущий элемент меньше опорного
            arr[i], arr[j] = arr[j], arr[i]  # Оxбмен местами
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Финальный обмен
    return i - 1  # Возвращаем индекс опорного элемента

def quicksort(arr, low, high):
    if low < high:
        q = partition(arr, low, high)  # Партирование
        quicksort(arr, low, q - 1)      # Рекурсивный вызов для левой части
        quicksort(arr, q + 1, high)     # Рекурсивный вызов для правой части

arr = [25, 17, 12, 21, 8, 14, 9, 27, 10, 4]
print("Исходный массив:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Отсортированный массив:", arr)