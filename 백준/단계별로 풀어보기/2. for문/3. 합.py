""" 이렇게 풀면 28776KB, 68ms
n = input()
n = int(n)
sum = 0
for i in range(1,n+1) :
    sum += i
print(sum)
"""
import sys
n = sys.stdin.readline()
n = int(n)
sum = 0
for i in range(1,n+1) :
    sum += i
print(sum)
# 이것도 똑같긴함...