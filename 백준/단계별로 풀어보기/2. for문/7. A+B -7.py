import sys
input = sys.stdin.readline

T = input()
T = int(T)

for i in range(0,T) :
    x, y = input().split()
    x = int(x)
    y = int(y)
    print(f"Case #{i+1}: {x+y}")