# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import json
import re
import random


def next_largest_brute(l):
    for i, n in enumerate(l):
        for j in range(i + 1, len(l)):
            if l[i] < l[j]:
                l[i] = l[j]
                break
        else:
            l[i] = -1
    return l


def is_cloud(skyMap, i, j):
    if i < 0 or i >= len(skyMap):
        return False
    if j < 0 or j >= len(skyMap[i]):
        return False
    return skyMap[i][j] == '1'


def countClouds(skyMap):
    count = 0
    visited = [[False for _ in row] for row in skyMap]
    for i, _ in enumerate(skyMap):
        for j, _ in enumerate(skyMap[i]):
            if visited[i][j] or not is_cloud(skyMap, i, j):
                continue
            count += 1
            s = [(i, j)]
            while s:
                x, y = s.pop()
                visited[x][y] = True
                for _x, _y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if is_cloud(skyMap, _x, _y) and not visited[_x][_y]:
                        s.append((_x, _y))

    return count


def pressingButtons(buttons):
    letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'j', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    if not buttons:
        return []

    if len(buttons) == 1:
        return letters[buttons[0]]
    b = buttons[0]
    s = pressingButtons(buttons[1:])
    return [_b + _s for _b in letters[b] for _s in s]


    # print(letters)

def stringPermutations(s):
    s = sorted(s)
    if not s:
        return []
    if len(s) == 1:
        return [s]
    s0 = s[0]
    substrings = stringPermutations(s[1:])
    output = []
    for i in range(len(s)):
        for sub in substrings:
            output.append(''.join(sub[0:i] + [s0] + sub[i:]))
    return output


def gcd(a, b):
    print ("entering")
    if not a:
        return b
    if not b:
        return a
    if a < b:
        a, b = b, a
    q = int(a / b)
    r = a - b * q
    return gcd(b, r)

#
# def wv2(island):
#     while len(island) > 1 and island[0] < island[1]:
#         island = island[1:]
#     while len(island) > 1 and island[-1] < island[-2]:
#         island = island[:-1]
#
#     m = island[0]
#     la

def water_volume(island):
    volume = 0
    s = []  # (0: position, 1: height)
    for i, height in enumerate(island):
        while s and s[-1][1] <= height:
            if len(s) > 1:
                pool_height = min(height, s[-2][1])
                volume += (pool_height - s[-1][1]) * (i - s[-2][0] - 1)
            s = s[:-1]  # i dont want to use an actual stack because i'm too lazy and high to look it up right now
        s.append((i, height))
    return volume


if __name__ == '__main__':
    arr = [-1, 0, -1, 0, -1, 0, -1]
    arr = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]
    print (water_volume(arr))
    pass


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
