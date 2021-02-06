import sys
input = sys.stdin.readline

s = list(input().upper().rstrip())

set_s = list(set(s))
set_s.sort()

cnt = []

for x in set_s :
    cnt.append(s.count(x))

if cnt.count(max(cnt)) > 1 :
    print("?")
else :
    print(s[cnt.index(max(cnt))])