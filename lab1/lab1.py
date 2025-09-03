def sortirovka(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        
        while i >= 0 and arr[i] > key:
            i -= 1
            
        arr[i + 1:j + 1] = [key] + arr[i + 1:j]

# array = [7, 2, 4, 9, 5, 1]
array = [3, 2, 8, 4, 7, 1]

sortirovka(array)
print(array)