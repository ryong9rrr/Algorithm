import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
print(min(num), max(num))