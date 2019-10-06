from collections import Counter

def superReducedString(s):
    ls = list(s)
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


def canExpand(grid, r, c, toExpandBy):
    if r <= 0 or r-toExpandBy < 0 or r > len(grid) or r+toExpandBy > len(grid):
        return False
    if c <= 0 or c-toExpandBy < 0 or c > len(grid[r]) or c+toExpandBy > len(grid[r]):
        return False
    if grid[r - toExpandBy][c] == 'B':
        return False
    if grid[r + toExpandBy][c] == 'B':
        return False
    if grid[r][c + toExpandBy] == 'B':
        return False
    if grid[r][c - toExpandBy] == 'B':
        return False
    if canExpand:
        return True


def getPluses(grid):
    pluses = []
    plus = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'G':
                plus.append([r, c])
                toExpandBy = 1
                while canExpand(grid, r, c, toExpandBy):
                    plus.append([r+toExpandBy, c])
                    plus.append([r, c+toExpandBy])
                    plus.append([r, c-toExpandBy])
                    plus.append([r-toExpandBy, c])
                    toExpandBy += 1
                pluses.append(plus)
            plus = []
    return pluses



def twoPluses(grid):
    pluses = getPluses(grid)
    nums = []
    for plus1 in pluses:
        compatible = True
        for plus2 in pluses:
            for square1 in plus1:
                for square2 in plus2:
                    if square1[0] == square2[0] and square1[1] == square2[1]:
                        compatible = False
            if compatible == True:
                nums.append(len(plus1) * len(plus2))
    return max(nums)



myGrid = [['G', 'G', 'G', 'G', 'G', 'G'],
         ['G', 'B', 'B', 'B', 'G', 'B'],
         ['G', 'G', 'G', 'G', 'G', 'G'],
         ['G', 'G', 'B', 'B', 'G', 'B'],
         ['G', 'G', 'G', 'G', 'G', 'G']]

print(twoPluses(myGrid))





