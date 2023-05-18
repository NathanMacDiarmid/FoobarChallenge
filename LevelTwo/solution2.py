def soltuion(s):
    salutes = 0
    for i, char in enumerate(s):
        if char == ">":
            salutes += s[i:].count("<")
    return salutes * 2

print(soltuion(">----<"))
print(soltuion(">>><<<"))
print(soltuion("<<>><"))
print(soltuion("--->-><-><-->-"))