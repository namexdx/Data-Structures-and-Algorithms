def max_heapify(A, i, heap_size):
    largest = i
    left = 2 * i + 1 
    right = 2 * i + 2 
    if left < heap_size and A[left] > A[largest]:
        largest = left
    if right < heap_size and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)

def build_heap(A):
    heap_size = len(A)
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(A, i, heap_size)

def heapsort(A):
    build_heap(A)
    heap_size = len(A)
    for i in range(heap_size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)

def heap_delete(A, i):
    if i < 1 or i > len(A):
        return "Индекс вне диапазона"
    
    A[i - 1] = A[-1]
    A.pop()
    max_heapify(A, i - 1, len(A)) 

if __name__ == "__main__":
    A = [25, 18, 5, 10, 15, 12, 3, 4, 2, 8, 6, 9, 7, 1]
    print("Исходный массив:", A)
    
    heap_delete(A, 3)
    print("Массив после удаления элемента с индексом 3:", A)

    heapsort(A)
    print("Отсортированный массив:", A)
