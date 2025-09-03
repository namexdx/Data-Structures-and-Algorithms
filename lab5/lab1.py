def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

array = [5, 0, 3, 5, 6, 0, 2, 3, 5, 3]
sorted_array = counting_sort(array)
print("Отсортированный массив (невозрастающий порядок):", sorted_array)