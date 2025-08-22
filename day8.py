def reverse_words(s):
    words = s.strip().split()
    words.reverse()
    result = " ".join(words)
    return result

s = "   the   sky   is blue   "
print(reverse_words(s))   
