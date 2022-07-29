import sys

sys.stdin = open("_최빈수구하기.txt")
T = int(input())

for test_case in range(T):
    number = int(input())
    score = list(map(int, input().split()))
    cnt = [0] * 101 # 0~100점까지 각각 몇명인지 세기
    
    for i in score:
        cnt[i] += 1
    
    most = 0
    ans = 0

    for k in range(1, len(cnt)):
        if ans <= cnt[k]: # 0점부터 순회하면서 최빈수를 찾는다. 
            ans = cnt[k] # <=로 썻기때문에 같은 최빈수일땐 더 높은 점수값으로 저장된다.
            most = k
    
    print(f'#{number} {most}')