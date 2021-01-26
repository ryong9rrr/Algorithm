import sys
input = sys.stdin.readline

T = input()
T = int(T)

for i in range(0,T) :
    for j in range(i, T-1) :
        print(" ", end="")
    for k in range(0,i+1) :
        print("*", end="")
    print()