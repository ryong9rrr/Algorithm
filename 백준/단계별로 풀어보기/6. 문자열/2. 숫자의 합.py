import sys
input = sys.stdin.readline

N = int(input())

numbers = input().rstrip()

if N == len(numbers) :
    result = 0
    for i in range(len(numbers)) :
        result += int(numbers[i])

    print(result)