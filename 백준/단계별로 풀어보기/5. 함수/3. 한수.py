import sys
input = sys.stdin.readline

N = int(input())
count = 0
for n in range(1, N+1) :
    if n < 100 :
        count += 1
    elif 100 <= n <= 1000 :
        num = [int(i) for i in str(n)]
        if num[0]-num[1] == num[1]-num[2] :
            count += 1

print(count)