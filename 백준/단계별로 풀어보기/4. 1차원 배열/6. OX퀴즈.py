import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    ox = input()
    temp_score = 0  # O그룹의 값을 저장하는 임시변수
    score = 0
    
    for i in range(len(ox)) :
        if ox[i] == 'O' :
            temp_score += 1
            score += temp_score

        elif ox[i] == 'X' :
            temp_score = 0

    print(int(score))