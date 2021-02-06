import sys
input = sys.stdin.readline

def get_number(s) : #s=알파벳
    x = ord(s)
    if x <= ord('C') :
        return 2
    elif x <= ord('F') :
        return 3
    elif x <= ord('I') :
        return 4
    elif x <= ord('L') :
        return 5
    elif x <= ord('O') :
        return 6
    elif x <= ord('S') :
        return 7
    elif x <= ord('V') :
        return 8
    elif x <= ord('Z') :
        return 9

result = 0
dials = list(input().rstrip())
for dial in dials :
    num = get_number(dial)
    result += num

print(result + len(dials))