#!/usr/bin/python
import sys

def josephus(n,k):
    x = list(range(1,n+1))  # for list [x1,x2)
    num = len(x)
    i = 0                   # current location!
    while num > 1 :
        i = (i+k-1)%num     # index to kick out
        print(x[i], end=' ')
        del x[i]
        num -= 1
    print(x[0])
    return x[0]


def main() :
    print("Please enter josephus ploblem of n and k :")
    line = sys.stdin.readline()
    x = line.split()
    josephus(int(x[0]),int(x[1]))


#The program entry for this script!
main()
