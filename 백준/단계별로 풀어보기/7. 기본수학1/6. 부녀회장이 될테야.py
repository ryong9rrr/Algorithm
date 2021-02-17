import sys
input = sys.stdin.readline

case = int(input())

for _ in range(case) :
    K = int(input())
    N = int(input())
    f0 = [n+1 for n in range(N)]

    for k in range(1, K+1) :
        for n in range(1, N) :
            f0[n] += f0[n-1]
            print(f0)
    print(f0[-1])