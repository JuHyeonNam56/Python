ItemsInCart = 0
#2개의 항목이 카트에 추가될 거임

if ItemsInCart != 2:
    #raise Exception("Products Cart count not matching")
    #raise는 "여기서 문제가 생겼으니 예외를 발생시켜라"라는 의미
    pass

#assert(ItemsInCart == 2) #assert(ItemsInCart == 2) AssertionError이라는 Error가 나오게 되는데 이 경우는 이미 위 함수가 0으로 선언이 되었기 때문에 2는 Error 가 나오게 됨
assert(ItemsInCart == 0)

#try/catch
#프로그램 도중 에러가 발생하더라도 프로그램이 멈추지 않고 처리할 수 있게 도와주는 기능
try:
    with open('filelog.txt', 'r')as reader: #이 렇게 존재하지 않는 파일이 나올 경우 except 를 입력하여 다른 선택지를 줌
        reader.read()

except:
    print("Some how i reached this block because there is failure in try block")

print("-------------------------------------------------------------------------------------------------")

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)



finally:
    print("cleaning up resources")
#finally를 사용하는 이유
#Test 실패와 상관없이 무조건 finally 함수를 타서 실행이 됨
#레코드를 지우거나 데이터를 정리하거나, 쿠키를 지우는데 필요한 레코드를 작성할 수 있음



