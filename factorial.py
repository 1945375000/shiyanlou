#!/usr/bin/env python3
import sys

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def div(n):
    return 10/n

def main(n):
    print(fact(n))

if __name__=='__main__':
    if len(sys.argv)>1:
        main(int(sys.argv[1]))
