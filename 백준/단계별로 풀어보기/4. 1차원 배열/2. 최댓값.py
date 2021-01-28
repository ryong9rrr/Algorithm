import sys
input = sys.stdin.readline

n_list = []
while len(n_list) != 9 :
    n = int(input())
    n_list.append(n)

print(max(n_list))
print(n_list.index(max(n_list))+1)