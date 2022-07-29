import sys

sys.stdin = open("_소득불균형.txt")
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    income = list(map(int, input().split()))
    avg_income = sum(income) / N #평균소득

    cnt = 0
    for i in income:
        if i <= avg_income: #입력된 income값을 순회하며 평균소득보다 낮은경우 cnt 추가
            cnt += 1
    print(f'#{test_case} {cnt}')
