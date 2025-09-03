def merge(A, p, q, r):
    C = []
    i = p
    j = q + 1
    
    while i <= q and j <= r:
        if A[i] < A[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(A[j])
            j += 1
            
    while i <= q:
        C.append(A[i])
        i += 1
    
    while j <= r:
        C.append(A[j])
        j += 1
    
    for k in range(len(C)):
        A[p + k] = C[k]

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)       
        merge_sort(A, q + 1, r)   
        merge(A, p, q, r)       

if __name__ == "__main__":
    A = [7, 3, 4, 9, 5, 1, 2, 6]
    print("Исходный массив:", A)
    merge_sort(A, 0, len(A) - 1)
    print("Отсортированный массив:", A)

    B = [5, 2, 8, 4, 7, 3, 1, 9]
    print("Исходный массив:", B)
    merge_sort(B, 0, len(B) - 1)
    print("Отсортированный массив:", B)