import sys


def maxtri(num):
    num.sort()
    if num[0] == 0:
        return
    while num[0]+num[1]<=num[2]:
        num[2]-=1
    c = num[0] + num[1] + num[2]
    return c


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    line = map(int, line.split(" "))
    print maxtri(line)
