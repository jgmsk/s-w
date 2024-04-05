'''
    작성일 : 2024 4월 5일
    작성자 : 컴퓨터 공학과 202495016 장민석
    설명 : 월을 입력받아 해당 계절을 출력하시오.
             3,4,5월 => 봄
             6,7,8월 => 여름
             9,10,11월 => 가을
             12,1,2월 => 겨울
             
            [문제분석]
                 필요한 변수: month
                 입력받는 월은 정수값이다.
                 월은 1~12 사이이다.
                 1~12 사이의 값이 (elif) 아니면 잘못된 월입니다.
                 봄, 여름, 가을, 겨울은 출력 값이다.
                 
                                  
             [알고리즘]   
                 1. 월을 입력 받는다.
                 2. 만약에 월이 3~5 사이라면
                     2-1. 봄을 입력 받는다.
                 3. elif 월이 6~8 사이라면 
                     3-1. 여름을 입력 받는다.
                 4. elif 월이 9~11 사이라면
                     4-1. 가을을 입력 받는다.
                 5. elif 월이 12,1,2 사이 이면
                     5-1.겨울을 출력한다.
                 6. else 아니면 
                     6-1. 잘못된 입력입니다.
'''
month = int(input(" 월을 입력 받는다. : "))

if month == 3 or month == 4 or month == 5 :
    print("봄 입니다.")
elif month == 6 or month == 7 or month == 8 :
    print("여름 입니다.")
elif month == 9 or month == 10 or month == 11 :
    print("가을 입니다.")
elif month == 12 or month == 1 or month == 2 :
    print("겨울 입니다.")
else :
    print("잘못된 값입니다.")