# Задача 1: Max_Heapify
def max_heapify(A, i, heap_size):
    largest = i
    left = 2 * i
    right = 2 * i + 1

    if left <= heap_size and A[left - 1] > A[largest - 1]:
        largest = left
    if right <= heap_size and A[right - 1] > A[largest - 1]:
        largest = right

    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        max_heapify(A, largest, heap_size)

A = [25, 18, 5, 10, 15, 12, 3, 4, 2, 8, 6, 9, 7, 1]
max_heapify(A, 3, len(A))
print("Результат после Max_Heapify:", A)

# Задача 2: Heapsort
def build_heap(A):
    heap_size = len(A)
    for i in range(heap_size // 2, 0, -1):
        max_heapify(A, i, heap_size)

def heapsort(A):
    build_heap(A)
    heap_size = len(A)
    for i in range(heap_size, 1, -1):
        A[0], A[i - 1] = A[i - 1], A[0]
        heap_size -= 1
        max_heapify(A, 1, heap_size)

A = [5, 7, 3, 9, 6, 8, 4, 1]
heapsort(A)
print("Отсортированный массив:", A)

# Задача 3: Heap_Delete
def heap_delete(A, i):
    if i < 1 or i > len(A):
        return "Индекс вне диапазона"

    A[i - 1] = A[-1] 
    A.pop() 
    max_heapify(A, i, len(A))

A = [25, 18, 5, 10, 15, 12, 3, 4, 2, 8, 6, 9, 7, 1]
heap_delete(A, 3)
print("Массив после удаления элемента с индексом 3:", A)