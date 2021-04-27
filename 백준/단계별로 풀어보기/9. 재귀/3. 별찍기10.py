import sys
input = sys.stdin.readline

def star(x, y, n) :
    if (x//n)%3==1 and (y//n)%3==1 :
        print(" ", end="")
    else :
        if n//3 == 0 :
            print("*", end="")
        else:
            star(x,y,n//3)


n = int(input())

for x in range(0, n) :
    for y in range(0, n) :
        star(x,y,n)
    print("")