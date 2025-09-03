def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        b = int(num // n)
        if b < len(arr):
            buckets[b].append(num)
        else:
            buckets[n-1].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

arr = [27, 1, 17, 32, 12, 8, 5, 19]
bucket_sort(arr)
print("Sorted array is:")
print(" ".join(map(str, arr)))
