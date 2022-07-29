import sys

sys.stdin = open("_신용카드만들기2.txt")
T = int(input())
validnum = ['3', '4', '5', '6', '9'] #시작번호 대조용 리스트

for test_case in range(1, T+1):
    cardnum = input()
    cardnum = cardnum.replace('-', '') # '-' 이 있으면 빼준다
    
    if cardnum[0] not in validnum: # 첫번호 34569 아닐경우 0 출력
        print(f'#{test_case} 0')
    elif len(cardnum) != 16: #16자리 숫자 아닐경우 0 출력
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')