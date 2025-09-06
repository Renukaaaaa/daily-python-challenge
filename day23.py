def sliding_window(arr, k):
    return [max(arr[i:i+k]) for i in range(len(arr)-k+1)]

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window(arr, k))  # [3, 3, 5, 5, 6, 7]
