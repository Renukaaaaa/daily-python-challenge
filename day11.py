from itertools import permutations

def string_permutations(s):
    perms = permutations(s)
    result = [''.join(p) for p in perms]
    return list(set(result))

s = "abc"
print(string_permutations(s))
