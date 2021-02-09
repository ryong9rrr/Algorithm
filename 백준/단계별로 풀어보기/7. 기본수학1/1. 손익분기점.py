import sys
import math
input = sys.stdin.readline

a, b, c = map(float, input().split())

if c-b > 0 :
    result = a / (c-b)
    print(math.floor(result)+1)
else :
    print("-1")