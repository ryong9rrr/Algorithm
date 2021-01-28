import sys
input = sys.stdin.readline

cycle = 0
num = int(input()) 
n = num
while True :
    ten = n // 10
    one = n % 10
    temp = ten + one
    n = int(str(one)+str(temp%10))
    cycle += 1
    if num == n :
        break
print(cycle)