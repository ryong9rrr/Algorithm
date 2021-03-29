import sys
import hashlib
input = sys.stdin.readline

s = input().rstrip()

result = hashlib.sha256(s.encode())

print( result.hexdigest() )