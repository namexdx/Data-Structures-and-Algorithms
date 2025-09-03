import random

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Случайный выбор опорного элемента
    print(pivot_index)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Перемещение опорного элемента в конец
    pivot = arr[high]
    
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:  # Сравниваем для невозрастающего порядка
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Обмен элементов
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Перемещение опорного элемента в правильное место
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)  # Разделение
        randomized_quicksort(arr, low, pi - 1)  # Рекурсивный вызов для левой части
        randomized_quicksort(arr, pi + 1, high)  # Рекурсивный вызов для правой части

# Пример использования
A = [4, 7, 9, 2, 6, 1, 3, 5]
print("Исходный массив:", A)
randomized_quicksort(A, 0, len(A) - 1)
print("Отсортированный массив (невозрастание):", A)