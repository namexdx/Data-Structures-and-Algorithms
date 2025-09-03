arr = []
path = r'el100_000_otsr_ob.txt'
l = 100_000
with open(path, 'r') as file:
    for i in range(l):
        arr.append(int(file.readline()))

start = time.time()
insert_sort(arr)
end = time.time()
print("Result: " + str((end-start)*1000))