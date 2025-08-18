def merge(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            arr2.sort()
    return arr1, arr2

arr1, arr2 = merge([1, 3, 5, 7], [2, 4, 6, 8])
print("arr1 =", arr1)
print("arr2 =", arr2)
