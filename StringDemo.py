str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[0]) #R
print(str[1]) #a
print(str[0:5]) #Rahul

print(str+str1)
print(str3 in str) #하위 문자열 확인하기

var = str.split(".") #.을 기준으로 글자 나누기
print(var)
print(var[0])
#문자열 빈 공간 없애기
str4 = " great "
print(str4.strip())
print(str4.lstrip())#오른쪽 공백만 없애기

print(str4.rstrip())#왼쪽 공백만 없애기

