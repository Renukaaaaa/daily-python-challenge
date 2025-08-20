def subarrays(arr):
    n = len(arr)
    result = []

    for start in range(n):
        total = 0
        for end in range(start, n):
            total += arr[end]
            if total == 0:
                result.append((start, end))
    return result

arr = [1, 2, -3, 3, -1, 2]
print("Input:", arr)
print("Output:",subarrays(arr))
