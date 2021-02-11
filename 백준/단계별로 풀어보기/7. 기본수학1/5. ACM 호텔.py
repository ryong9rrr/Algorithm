import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    h, w, n = map(int, input().split())

    x = n % h
    y = (n // h) + 1

    if x == 0 :
        x = h
        y = n // h

    print(str(x)+str(y).zfill(2))
    #print(str(x)+str(y).rjust(2, "0"))