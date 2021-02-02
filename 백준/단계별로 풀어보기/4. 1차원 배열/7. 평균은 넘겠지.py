import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C) :
    data_list = list(map(int, input().split()))
    N = data_list[0]
    
    del data_list[0]
    avg = sum(data_list) / N

    count = 0
    for i in range(N) :
        if data_list[i] > avg :
            count += 1
    
    result = format(count / N * 100, ".3f")
    print(f"{result}%")