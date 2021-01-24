""" 시간초과
T = input()
T = int(T)

for i in range(0, T) :
    x, y = input().split()
    x=int(x)
    y=int(y)
    print(f"{x+y}")
"""
""" 런타임에러
T = sys.stdin.readline()
T = int(T)

for i in range(0, T) :
    x, y = sys.stdin.readline().split()
    x=int(x)
    y=int(y)
    print(f"{x+y}")
"""
# input = sys.stdin.readline 치환을 하면 더 빨라진다.
import sys
input = sys.stdin.readline
T = input()
T = int(T)

for i in range(0, T) :
    x, y = input().split()
    x=int(x)
    y=int(y)
    print(f"{x+y}")