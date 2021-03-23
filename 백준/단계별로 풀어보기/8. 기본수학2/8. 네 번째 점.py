import sys
input = sys.stdin.readline

x, y = 0, 0
for _ in range(0,3) :
    A, B = map(int, input().split())
    x ^= A
    y ^= B

print(x, y)