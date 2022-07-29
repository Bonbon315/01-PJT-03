import sys

sys.stdin = open("_직사각형길이찾기.txt")
T = int(input())

for test_case in range(1, T+1):
    rect = list(map(int, input().split()))
    rect.sort() # 일단 정렬부터 한다
    ans = 0

    if rect[0] != rect[1]: #첫번째, 두번째가 다르다면 첫번째 숫자가 짝이 없는것이기때문에 첫번째가 답
        ans = rect[0]
    else: # 그외엔 모든 경우의 수에서 마지막 숫자가 답이다
        ans = rect[2]
    
    print(f'#{test_case} {ans}')

