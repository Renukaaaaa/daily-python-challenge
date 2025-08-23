def CommonPrefix(strs):
    if not strs:
        return ""

    result = ""
    for i in range(len(min(strs, key=len))):  
        char = strs[0][i]
        if all(s[i] == char for s in strs):
            result += char
        else:
            break
    return result

strs = ["flower", "flow", "flight"]
print(CommonPrefix(strs)) 
