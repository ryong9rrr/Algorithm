import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

'''
a = h-y if h-y < y else y
b = w-x if w-x < x else x

result = a if a<b else b
'''
print( min([x, y, w-x, h-y]) )