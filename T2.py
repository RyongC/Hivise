import numpy as np

rw = 8
col = 2

arr = np.full(shape = (40, 40), fill_value = 99)

arr1 = np.full(shape = (40, 40), fill_value = 1)
arr2 = np.full(shape = (40, 40), fill_value = 2)


for r in range(rw):
    for c in range(col):
        arr[r][c] = arr2[r][c]

print(arr)
# arr2 =
# arr10 =


# print(arr1)