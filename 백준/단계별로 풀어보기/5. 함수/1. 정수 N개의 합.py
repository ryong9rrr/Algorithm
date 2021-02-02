import sys
input = sys.stdin.readline

def solve(a) :
    return print(sum(a))


a = list(map(int, input().split()))

solve(a)