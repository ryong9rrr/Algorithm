import sys
input = sys.stdin.readline

words = list(input().upper().rstrip())

words.sort()

print(words)
