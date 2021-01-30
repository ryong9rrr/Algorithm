import sys
input = sys.stdin.readline

num_list = []
for input_num in range(10) :
    input_num = int(input())
    result = input_num % 42
    num_list.append(result)

print(len(set(num_list)))