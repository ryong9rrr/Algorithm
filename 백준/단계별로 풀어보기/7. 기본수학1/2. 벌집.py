import sys
input = sys.stdin.readline

N = int(input())

num = 1
i = 0
while num < N :
    i += 1
    num += 6*i

print(i+1)