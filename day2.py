def find_missing(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)

arr = [1, 2, 4, 5]
print("Missing number is:", find_missing(arr))
