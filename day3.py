def findDuplicate(arr):
    duplicate = set()
    for num in arr:
        if num in duplicate:
            return num
        duplicate.add(num)
        
arr = [3, 1, 3, 4, 2]
print("Duplicate number:", findDuplicate(arr))
