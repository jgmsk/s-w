'''
    작성일 : 2024 4월 19일
    작성자 : 컴퓨터 공학과 202495016 장민석
    설명 : 구구단 전체를 출력하시오.
        
     [문제분석]
         단은 2단 ~ 9단까지
         곱하는 수는 1 ~ 9까지
         2단 => 2 * 1 = 2   2 * 2 = 4 . . .
         3단 => 3 * 1 = 3   3 * 2 = 6 . . .
         
         2단을 기준으로 곱하는 수가 1~9까지 반복을 끝내면
         단을 1 증가하여 다음 단을 곱하는 수 1~9까지 반복한다.
         
         단을 반복하면서 곱하는 수 를 반복한다.
         반복을 이중으로 사용한다.
         
        
     [알고리즘]
         1. 단은 2단부터 9단까지 반복한다.
             1-1. 곱하는 수는 1부터 9까지 반복한다.
                 1-1-1. 단 * 수 = 결과 출력
'''
for dan in range(2, 10) :
    print(f"== {dan}단 ==")
    for su in range(1, 10) :
        print(f"{dan} x {su} = {dan*su}")