import sys

sys.stdin = open("_암호문1.txt")
for test_case in range(1, 11):
    N = int(input())
    original = list(map(int, input().split()))
    #449047 855428 425117 532416 358612 929816 313459 311433 472478 589139 568205

    P = int(input())

    order = list(input().split())
    #I 1 5 400905 139831 966064 336948 119288

    for i in range(len(order)):
        if order[i] == 'I':
            insert_idx = int(order[i+1]) # 1
            insert_count = int(order[i+2]) # 5
            insert_list = list(order[i+3:i+3+insert_count]) # 400905 139831 966064 336948 119288
            for k in range(insert_count):
                original.insert(insert_idx+k,insert_list[k]) # 1, 400905 / 2, 139831 / ...
                
    print(f'#{test_case} ', end='')
    for i in range(10): 
        print(original[i], end=' ')
    print()
    #리스트에서 숫자만 빼서 출력하는 방법이 기억이 안남. 
    #.join인건 기억하는데 상세 문법이 기억이 안나서 일단 되는대로 구현했다.