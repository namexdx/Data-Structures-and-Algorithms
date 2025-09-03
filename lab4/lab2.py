def partition(arr, low, high):
    x = arr[low]  # Опорный элемент (первый элемент)
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < x:  # Для сортировки в неубывающем порядке
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Финальный обмен
    return i - 1

def quicksort(arr, low, high):
    if low < high:
        q = partition(arr, low, high)
        quicksort(arr, low, q - 1)
        quicksort(arr, q + 1, high)

arr = [4, 7, 9, 2, 6, 1, 3, 5]
print("Исходный массив:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Отсортированный массив:", arr)