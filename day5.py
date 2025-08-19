arr = [16, 17, 4, 3, 5, 2]
leaders = []

for i in range(len(arr)):
    if all(arr[i] > x for x in arr[i+1:]):  
        leaders.append(arr[i])

print("Leaders:", leaders)
