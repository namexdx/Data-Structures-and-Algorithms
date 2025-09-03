def counting_sort_for_radix(arr, exp):
    output = ["" for _ in arr]
    count = [0] * 26 

    for string in arr:
        index = ord(string[-exp]) - ord('a')
        count[index] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for string in reversed(arr):
        index = ord(string[-exp]) - ord('a')
        output[count[index] - 1] = string
        count[index] -= 1

    return output

def radix_sort(arr):
    max_length = max(len(string) for string in arr)
    for exp in range(1, max_length + 1):
        arr = counting_sort_for_radix(arr, exp)
    return arr

array = ["dog", "end", "box", "day", "the", "man", "ask", "tea", "cat", "mob"]
sorted_array = radix_sort(array)
print("Отсортированный массив (невозрастающий порядок):", sorted_array)