import sys
input = sys.stdin.readline

T = input()
T = int(T)

for i in range(0,T) :
    for j in range(0, i+1) :
        print("*", end="")
    print()