""" 28776KB, 72ms
num = input()
num = int(num)
for i in range(0,num) :
    x, y = input().split()
    x = int(x)
    y = int(y)
    print(f"{x+y}")
"""
# 28776KB, 64ms
import sys
num = sys.stdin.readline()
num = int(num)
for i in range(0,num) :
    x, y = sys.stdin.readline().split()
    x = int(x)
    y = int(y)
    print(f"{x+y}")
