import sys
input = sys.stdin.readline

M = 1234567891
#_hash_list = [None] * M

L = int(input())
S = input().rstrip()

_hash = 0
for i in range(0, len(S)) :
    _hash += (ord(S[i])-96) * (31**i)
    _hash %= M

#_hash_list.insert(_hash, S)

print( _hash )