import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

day = 0
loc = 0

while True :
    day += 1
    loc += A
    if loc < V :
        loc -= B
    elif loc >= V :
        break

print(day)

#달팽이.. 시간초과

import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

day = 1
loc = A

while loc < V :
    loc -= B
    day += 1
    loc += A

print(day)

# 이것도 시간초과