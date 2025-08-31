def prime_factorization(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

N = 18
print("Input:", N)
print("Output:", prime_factorization(N))
