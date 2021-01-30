import sys
input = sys.stdin.readline

N = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)

for i in range(N) :
    score_list[i] = (100 * score_list[i] / max_score)

print(round(sum(score_list)/N, 6))