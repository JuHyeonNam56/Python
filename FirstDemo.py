print("hello")

# 주석으로 이것은 감지되지 않습니다.

a = 3 #변수 선언
print(a)#선언된 변수를 출력

str = "hello world" #문자열 선언

print(str)

b, c, d = 5, 6.4, "Gear"

#print("Value is"+b)
# #파이썬은 엄격한 자료형 통합을 가지고 있어서 위의 내용처럼 다른 자료형을 같이 입력을 할 수 없음


#문자열과 정수를 연결하는 방법은 우선 중괄호와 따음표를 입혀야 함
"{} {}".format("Value is", b)

#출력 결과 확인
print("{} {}".format("Value is", b))

#각 변수가 가지고 있는 자료형의 종류 파악
print(type(b))

print(type(c))
print(type(d))

