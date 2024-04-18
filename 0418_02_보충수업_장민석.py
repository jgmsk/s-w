'''
    작성일 : 2024 4월 18일
    작성자 : 컴퓨터 공학과 202495016 장민석
    설명 : 사용자로부터 정수를 입력받아 그 정수의 약수를 찾아 주시오.
        
     [문제분석]
         1. 사용자로 부터 정수를 입력받는다.
         2. 수가 약수인지 아닌지 판별 한다.
         3. 약수는 나머지 없이 나눌 수 있는 수, 쪽 나머지가 0이 되는 수 이다.
         4. 1부터 입력 받은 수까지 나누었을때 나머지가 0이 되는 수 도출 도출된 수를 입력
         
        
     [알고리즘]
         1. 정수 입력 받는다.
         2. 1부터 입력 받은 수까지 나누었을때 (나머지가 0이 되는 수)
         3. 해당 되는 수 모두 출력한다.
'''

input_num = int(input("정수를 입력받는다."))

print(f"{input_num}의 약수는 ", end='')

print("== for ==")
for num in range(1, input_num+1) :
    if input_num % num == 0 :
        print(num, end=', ')
        
print()

print("== while ==")
num = 1
while num <= input_num :
    if input_num % num == 0 :
        print(num, end=', ')
    num = num + 1