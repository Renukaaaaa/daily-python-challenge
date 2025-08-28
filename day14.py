def count_substrings(s, k):
    n = len(s)
    result = 0

    for i in range(n):
        distinct_chars = set()
        for j in range(i, n):
            distinct_chars.add(s[j])
            if len(distinct_chars) == k:
                result += 1
            elif len(distinct_chars) > k:
                break 
    
    return result

s = "pqpqs"
k = 2
print(count_substrings(s, k))  
