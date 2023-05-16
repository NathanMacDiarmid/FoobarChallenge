def solution(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    xARR = list(x)
    result = ""
    for i in xARR:
        if (i.isupper()):
            result += i
        elif (i.islower()):
            letterIndex = alphabet.index(i)
            result += alphabet[(letterIndex * -1) - 1]
        else:
            result += i
    return result

print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))