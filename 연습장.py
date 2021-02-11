import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    H, W, N = map(int, input().split())

    if N%H != 0 :
        x = str(N % H)

        if (N//H)+1  < 10 :
            y = '0'+str((N // H) + 1)
        elif (N//H)+1 >= 10 :
            y = str((N // H) + 1)

    elif N%H == 0 :
        x = str(H)
        if N//H < 10 : 
            y = '0'+ str(N//H)
        elif N//H >= 10 :
            y = str(N//H) 

    print(x+y)