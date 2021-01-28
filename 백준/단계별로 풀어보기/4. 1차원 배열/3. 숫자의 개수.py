import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
result = str(A*B*C)

new_list = list()
for i in range(len(result)) :
    new_list.append(int(result[i]))

for i in range(0, 10) :
    print(new_list.count(i))