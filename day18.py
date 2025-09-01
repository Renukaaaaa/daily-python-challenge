import math
def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n // i:   
                count += 1
            else:
                count += 2
    return count

N = int(input("Enter a number: "))
print(count_divisors(N))