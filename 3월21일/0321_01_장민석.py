'''
    작성일 : 2024 3월 21일
    작성자 : 컴퓨터 공학과 202495016 장민석
    설명 : 변수 사용과 출력 함수 사용하기
'''
# 정수 10을 변수에 저장하시오.
num = 10

# 3.14를 변수에 저장하시오.
pi = 3.14

# 자기 이름을 변수에 저장하시오.
name = "장민석"

# 각 변수에 저장된 값을 출력하시오.
# 출력을 할 떄는 친절하게 하자!!!
print("num에 저장된 값 : ", num)
print("num에 저장된 값 : {}" .format(num))
print(f"num에 저장된 값 : {num}")

print("pi변수에는 원주율", pi, "가 있습니다.")
print("pi변수에는 원주율 {}가 있습니다." .format(pi))
print(f"pi변수에는 원주율 {pi}가 있습니다.")

print("제 이름은 ",name, "입니다.")
print("제 이름은 {}입니다." .format(name))
print(f"제 이름은 {name}입니다.")

# 변수의 자료형 알아보기
# type() 함수 사용하기
print("num의 자료형 : ", type(num))
print("pi의 자료형 : ", type(pi))
print("name의 자료형 : ", type(name))