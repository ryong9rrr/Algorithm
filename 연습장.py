import sys
input = sys.stdin.readline

x = '0'
result = ''
cycle = 0
while x != result :
    cycle += 1
    if 10 <= int(x) <= 99 :
        result = x[1] + str( int(x[0]) + int(x[1]) )[:-1]
    elif 0 <= int(x) < 10 :
        result = str(int(x+x))
    

print(cycle)




import sys
input = sys.stdin.readline
cycle = 0

input_number = input()
number = int(input_number)

result = ""
zero = ""
one = ""

while True :
    cycle += 1
    
    if 10 <= int(result) <= 99 :
        zero = result[0]
        one = result[1]
        temp = str(int(zero)+int(one))
        result = one + temp[:-1]

    elif 0 <= int(result) < 10 :
        result = result + result

    result = int(result)

print(cycle)
