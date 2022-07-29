import sys

sys.stdin = open("_신용카드만들기1.txt")
T = int(input())

for test_case in range(1, T+1):
    cardnum = list(map(int, input().split()))
    luhn = 0

    for i in range(1, len(cardnum)+1):
        if i%2 == 1:
            luhn += cardnum[i-1]*2 #예문에서 주어진 공식대로 룬 공식값 저장
        else:
            luhn += cardnum[i-1]

    ans = (10 - luhn % 10) % 10 #10을 0으로 바꾸려면 이렇게 해야한다.
    print(f'#{test_case} {ans}')