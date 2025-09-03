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

if __name__ == "__main__":
    A = [25, 18, 5, 10, 15, 12, 3, 4, 2, 8, 6, 9, 7, 1]
    print("Результат после Max_Heapify:", A)