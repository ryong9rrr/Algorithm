import sys
input = sys.stdin.readline

N = int(input())

# N이 몇번 line에 있는지 구한다.
# line 은 N이 존재하는 line넘버, sum_line은 전 line까지의 합
line = 0
sum_line = 0
while sum_line < N :
    line += 1
    sum_line += line

sum_line = sum_line - line

if line%2 == 1 :
    b = N - sum_line
    a = line - b + 1

    print(f"{a}/{b}")

elif line%2 == 0 :
    a = N - sum_line
    b = line - a + 1

    print(f"{a}/{b}")