Values = [4, 65, "Zero", 5, 2]
#List형은 무조건 대괄호를 써야함 -> 이건 당연한 이야기
#List는 자료형이며 다른 자료형을 포함하여 여러 값을 허용

print(Values[0])
print(Values[3])

print(Values[-1])
#-1은 마지막 인덱스를 가르킴
print(Values[1:3])
#하위 리스트를 구하는 방법 2~3까지

Values.insert(3,"QA")
#insert로 삽입을 진행 3번 인덱스 뒤에 Shetty 를 삽입한다는 의미
print(Values)

Values.append("End")
#끝 부분에 새로운 Index 값 삽입
print(Values)

#Values[2] = "RAHUL"
#Index 값을 업데이트 -> 소문자였던 문자열을 대문자로 변경
print(Values)

del Values[0]
print(Values)
#Index 삭제

#Tuple 자료형은 불변이지만 리스트 자료형은 불변이 아님 (Tuple은 업로드가 안됨)
val = (1, 2, "example", 4.5)
print(val[1])
val[2] = "Test"
#이렇게 입력을 하면 Error 가 나오게 되는데 이것은 Tuple이 변경을 하지 못한다고 안내를 해주는 것
print(val)
#Tuple과 List와 관련하여 딕셔너리를 선언 이 부분은 중괄호를 사용
#list -> 대괄호 / Tuple -> 소괄호 / 딕셔너리 -> 중괄호
dic = {"a":2 , 4:"abc", "c":"hello world"}
print(dic[4])
print(dic["c"])


dict = {

}

dict["firstname"] = "Man"
dict[
    "lastname"
] = "Boy"
dict[
    "gender"
] = "male"
print(dict)
print(dict["lastname"])