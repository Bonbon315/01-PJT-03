import sys

sys.stdin = open("_문자열의거울상.txt")
T = int(input())
original = ['b', 'd', 'p', 'q']
mirror = ['d', 'b', 'q', 'p']

for test_case in range(1, T+1):
    word = input()
    word = word[::-1] #먼저 입력된 문자열 뒤집고 시작
    ans = ''
    for i in word:
        ans += mirror[original.index(i)] #위에서 정의한 리스트를 index 값으로 대조하여 ans에 추가
    print(f'#{test_case} {ans}')