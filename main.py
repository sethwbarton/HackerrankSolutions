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


def twoPluses(grid):
    biggestPlus = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            area = 0;
            expandability = 0
            canExpand = True
            if grid[r][c] == 'G':
                area = 1
            while canExpand:
                if grid[r - expandability][c] == 'B':
                    canExpand = False
                if grid[r + expandability][c] == 'B':
                    canExpand = False
                if grid[r][c + expandability] == 'B':
                    canExpand = False
                if grid[r][c - expandability] == 'B':
                    canExpand = False
                if canExpand:
                    if expandability > 0:
                        area += 4
                    expandability += 1
            if area > biggestArea:
                biggestArea = area
                biggestPlus = [[r, c]]
                while canExpand:
                    if grid[r - expandability][c] == 'B':
                        canExpand = False
                    if grid[r + expandability][c] == 'B':
                        canExpand = False
                    if grid[r][c + expandability] == 'B':
                        canExpand = False
                    if grid[r][c - expandability] == 'B':
                        canExpand = False
                    if canExpand:
                        if expandability > 0:
                            area += 4
                            biggestPlus.push([r - expandability][c])
                            biggestPlus.push([r + expandability][c])
                            biggestPlus.push([r][c + expandability])
                            biggestPlus.push([r][c - expandability])
                        expandability += 1
        for square in biggestPlus:
            grid[square[0]][square[1]] = 'B'
    print(biggestPlus)


grid = [['G', 'G', 'G', 'G', 'G', 'G'],
        ['G', 'B', 'B', 'B', 'G', 'B'],
        ['G', 'G', 'G', 'G', 'G', 'G'],
        ['G', 'G', 'B', 'B', 'G', 'B'],
        ['G', 'G', 'G', 'G', 'G', 'G']]

twoPluses(grid)

