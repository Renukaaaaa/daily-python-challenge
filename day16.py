import math

def find_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

N = 4
M = 6
print("LCM of", N, "and", M, "is:", find_lcm(N, M))
