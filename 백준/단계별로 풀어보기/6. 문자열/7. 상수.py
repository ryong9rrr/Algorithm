import sys
input = sys.stdin.readline

a, b = input().split()

rev_a = int(a[::-1])
rev_b = int(b[::-1])

result = rev_a if rev_a>rev_b else rev_b

print(result)