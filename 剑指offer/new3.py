import sys


def min(s):
    n = len(s)
    r = 0
    count = 0
    if s is None:
        return
    for i in range(0,n):
        if s[i] is 'R':
            r += 1
    if r == n:
        return 0
    if r == 0:
        return
    for i in range (0,r):
        if s[i] is not 'R':
            count += 1
    return count*2


if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    print min(line1)
