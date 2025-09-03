def merge(A, p, q, r):
    size = r - p + 1
    C = [0] * size 
    
    print(f"Объединение подмассивов A[{p}..{q}] и A[{q + 1}..{r}]")
    
    i = p
    j = q + 1
    k = 0

    while i <= q and j <= r:
        if A[i] < A[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = A[j]
            j += 1
        k += 1

    while i <= q:
        C[k] = A[i]
        i += 1
        k += 1

    while j <= r:
        C[k] = A[j]
        j += 1
        k += 1

    for l in range(size):
        A[p + l] = C[l]

    print(f"Результат после объединения: {A[p:r + 1]}")

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

A = [38, 27, 43, 3, 9, 82, 10]
print(f"Начальный массив: {A}")
merge_sort(A, 0, len(A) - 1)
print(f"Отсортированный массив: {A}") 