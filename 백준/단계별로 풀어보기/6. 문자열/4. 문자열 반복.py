import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    test = input().split()
    R = int(test[0])
    del test[0]
    S = test[0]
    
    for i in range(len(S)) :
        for j in range(R) :
            print(S[i], end="")

    print(end="\n")