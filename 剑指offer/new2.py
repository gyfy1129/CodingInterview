import sys

def fly_number(num1,num2):
    count = 0
    flight = 0
    n = len(num2)
    for i in range(0,n):
        if flight <= num1[1]:
            flight = flight + num2[i]
            count += 1
    return count



if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    line1 = map(int, line1.split(" "))
    line2 = sys.stdin.readline().strip()
    line2 = map(int, line2.split(" "))
    print fly_number(line1,line2)