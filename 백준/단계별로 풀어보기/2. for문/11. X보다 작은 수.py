import sys
input = sys.stdin.readline

N, X = map(int, input().split())
n_list = list(map(int, input().split()))

if len(n_list) > N :
        print(f"입력한 숫자가 너무 많습니다.")
else :
    for i in range(0,N) :
        if n_list[i] < X :
            print(f"{n_list[i]}", end=" ")