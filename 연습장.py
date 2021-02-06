s = input().lower()
s_list = list(set(s))
cnt = []
for x in s_list:
    count = s.count(x)
    print(count)