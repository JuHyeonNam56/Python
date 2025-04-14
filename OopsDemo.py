#클래스란? 사용자 정의된 청사진 또는 프로토타입
#sum, multiplication, addtion, constant
#Class 는 기본적으로 메소드, 변수 또는 클래스 변수, 인스턴스 변수, 생성자가 있음

class Calculator:
    num = 100 #클래스 변수
    #아무것도 정의하지 않는 경우, 기본 생성자가 호출이 됨
    #생성자 만들 때 구문(__입력


    def __init__(self,a,b):
        self.firstNumber=a
        self.secondNumber=b
        print("I am clled automatically when object is created")
#self 가 붙는 이유는 파이썬은 무엇이 호출하는지에 관한 객체 참조 -> 혼자서는 호출 할 수 없음
    def getData(self):
        print("i am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num #클래스의 경우는 무조건 참조 변수 self 를 넣어줘야 하지만 객체의 경우에는 넣어줄 필요가 없음

obj = Calculator(2, 3) #파이썬에서 객체를 생성하는 구문
obj.getData()
print(obj.Summation())

#생성자는 클래스의 객체를 생성할 때 자동으로 호출되는 메소드 -> self 설명
obj1 = Calculator(4, 5) #파이썬에서 객체를 생성하는 구문
obj1.getData()
print(obj1.Summation())

#self 키워드는 변수 이름을 메소드로 호출하는데 필수 입니다.
#인스턴스 및 클래스 변수는 완전히 다른 목적을 갖고 있습니다.
#하나는 객체에 첨부되고 다른 하나는 객체에 첨부되지 않습니다.
#생성자 이름은 반드시 __init__이여야 합니다.
#객체를 생성할 때는 새로운 키워드는 필요하지 않습니다.