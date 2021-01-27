import sys
input = sys.stdin.readline

while True :
    try:
        x, y = map(int, input().split())
    except:
        break
    print(x+y)