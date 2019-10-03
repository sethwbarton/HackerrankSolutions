from collections import Counter

def superReducedString(s):
    ls = list(s);
    for ch in range(len(ls)):
        if ch <= len(ls) - 2:
            if ls[ch] == ls[ch+1]:
                del ls[ch]
                del ls[ch+1]
                ch = 0
    if len(ls) == 0:
        return "Empty String"
    else:
        return "".join(ls)


def anagram(s):
    if len(s) % 2 != 0:
        return -1;
    str1 = list(s[0:int(len(s) / 2)])
    str2 = list(s[int(len(s) / 2):len(s)])
    return sum(max(0, str2.count(c) - str1.count(c)) for c in set(str2))



