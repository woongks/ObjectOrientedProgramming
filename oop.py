''' 
객체 지향 프로그래밍

객체란? 우리가 살아가면서 보는 모든 존재를 말한다.

객체는 속성과 행동으로 이루어져 있다.

객체 지향 프로그래밍이란 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로

파악하는 프로그래밍 접근법이다.

즉, 프로그램을 객체들과 객체들 간의 소통으로 바라본다.

예를 들어서 총 게임에서 게임 캐릭터는 하나의 객체. 총은 또 하나의 객체. 총알도 객체이다.

객체지향적으로 설계했다 = 모델링을 했다.

객체 지향 프로그래밍으로 프로그램을 만들려면

1. 프로그램에 어떤 객체들이 필요할지 정한다.
2. 객체들의 속성과 행동을 정한다.
3. 객체들이 서로 어떻게 소통할지 정한다. 
'''


'''
Unit 1: 객체 지향 프로그래밍이란?
객체 지향 프로그래밍을 위한 준비!

객체 지향 프로그래밍이 무엇이고 왜 중요한지를 알아가는 시간입니다. 객체와 클래스의 개념을 이해하고 파이썬에서 클래스를 어떻게 정의하고 사용하는지 공부합니다.

Chapter 1: 객체 지향 프로그래밍 시작하기
Chapter 2: 객체를 만드는 법
Chapter 3: 미리 알고가야 할 것들
Chapter 4: 객체 만들기 연습
Chapter 5: 객체 지향 프로그래밍 직접 해보기
Unit 2: 객체 지향 프로그래밍의 4가지 기둥
객체 지향 프로그래밍을 하기 위한 필수 개념 익히기!

객체 지향 프로그래밍을 하기 위해 꼭 알아야할 4가지 개념을 배우고 실습합니다.

Chapter 1: 추상화(Abstraction)
Chapter 2: 캡슐화(Encapsulation)
Chapter 3: 상속(Inheritance)
Chapter 4: 다형성(Polymorphism)
Unit 3: 견고한 객체 지향 프로그래밍: SOLID 원칙
유지보수하기 쉬운 코드를 만들자!

이제 객체 지향 프로그래밍을 어떻게 하는지는 배웠습니다. 하지만 단순히 할 줄 아는 것만으로는 부족합니다. 객체 지향 프로그래밍을 할 때 어떻게 유지보수하기 쉬운 코드를 만들 수 있는지를 알아야 합니다. 이를 위한 대표적인 객체 설계의 원칙 5가지를 설명합니다.

Chapter 1: 단일 책임 원칙 (Single Responsibility Principle)
Chapter 2: 개방 폐쇄 원칙 (Open-closed Principle)
Chapter 3: 리스코프 치환 원칙 (Liskov Substitution Principle)
Chapter 4: 인터페이스 분리 원칙 (Interface Segregation Principle)
Chapter 5: 의존 관계 역전 원칙 (Dependency Inversion Principle)
'''

'''
인스타그램의 유저를 객체로 만든다고 하면 속성과 행동은 다음과 같다:
속성 -> 이름, 이메일주소, 비밀번호, 팔로우 목록, 팔로워 목록
행동 -> 자기소개하기, 팔로우하기

객체의 틀을 class라고 한다.
객체는 instance라고 한다.
class 첫글자는 항상 대문자이다.

객체의 속성은 변수, 행동은 함수, 혹은 메소드라고 한다.

메소드 종류는

1. 인스턴스 메소드
2. 클래스 메소드
3. 정적 메소드

3가지로 구성된다.
'''
'''
class User:
    def say_hello(self):
        print('안녕하세요 저는 {}입니다.'.format(self.name))
    def login(self, my_email, my_password):
        if self.email == my_email and self.password == my_password:
            print('로그인 성공, 환영합니다.')
        else:
            print('로그인 실패')
    def check_name(self,name):
        return self.name == name

user1 = User()
user1.name = '김대위'
user1.email = 'captain@naver.kr'
user1.password = '12345'

user2 = User()
user2.name = '김말이'
user2.email = 'marie@yahoo.kr'
user2.password = '1e345'

print(user1.email)
print(user2.password)

User.say_hello(user1)    #클래스에서 메소드를 호출
user1.say_hello()    # 인스턴스의 메소드로 호출
user1.login('captain@naver.kr','12345')
User.login(user1,'captain@naver.kr','12345')'''

# 글자 앞뒤로 언더바가 두 개씩 있는 함수를 magic method / special method 라 한다.
# 혹은 특수 메서드라고 한다. 특정 상황에서 자동으로 호출되는 함수이다.
# 예를 들어 init은 class 생성시 자동으로 호출되는 함수이다.


# 클래스 밑에 정의한 것을 클래스 변수라고 한다.

class User:
    count = 0 # 클래스 변수
    # 유저 인스턴스의 모든 변수를 지정해주는 메소드
    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw
        User.count += 1
    def say_hello(self):
        print('안녕하세요 저는 {}입니다.'.format(self.name))
    #우리가 인스턴스를 출력하면 메모리 주소만 나오는 것을 바꾸자
    def __str__(self):
        return '사용자: {}, 이메일: {}, 비번: *****'.format(self.name,self.email)
    @classmethod
    def number_of_users(cls): # 첫 파라미터는 무조건 cls로 쓰기
        cls.count # User.count와 동일하다
        print('총 유저 수는: {}입니다'.format(cls.count))
    
    @classmethod
    def string_to_value(cls,string):
        string_list = string.split(',')
        name = string_list[0]
        email = string_list[1]
        password = string_list[2]
        return cls(name,email,password)
    

user1 = User('김말이', 'abc@def.kr','1234')
user2 = User('김말삼', 'aabc@deddf.kr','12134')
user3 = User('김말사', 'abdeeqc@ddsef.kr','12q22134')
#클래스 메소드와 인스턴스 메소드의 차이
# 인스턴스 메소드에서는 인스턴스로 호출을 해야 자신이 첫 번째 파라미터로 자동 전달된다.
# 클래스 메소드는 모두 첫번째 파라미터로 클래스가 자동 전달 된다.
# 인스턴스 변수를 쓰지 않는 함수는 클래스 메서드로 만든다.
# 인스턴스 변수를 하나도 정의하지 않았을 경우도 포함이다.

print(User.count)
User.number_of_users()
user1.number_of_users()
# 만약에 user1.count = 5를 지정해주면 이는 user1의 count만 5로 바꿔준다.
# 같은 이름의 클래스 변수와 인스턴스 변수가 있으면 인스턴스 변수를 읽는다.

#데코레이터란?
# 함수를 꾸며서 새로운 함수로 만든다.

def print_hello():
    print('안녕하세요')

def add_print_to(original):
    def wrapper():
        print('함수 시작')
        original()
        print('함수 끝')
    return wrapper

add_print_to(print_hello)()

# 위와 동일한 다른 방법

@add_print_to                   #밑의 함수를 add_print_to로 꾸며라
def print_hello():
    print('안녕하세요')

print_hello()

#정적 메소드
#정적 메소드는 인스턴스, 클래스 변수를 전혀 다루지 않는 메소드이다.
# 인스턴스나 클래스 변수를 사용하지 않을 때 정적 메소드를 쓴다.
# 데코레이터를 붙이지 않으면 self가 첫 파라미터로 들어가기 때문에
# @staticmethod를 붙여준다.


#파이썬은 순수 객체 지향 언어이다.
# 가변 타입 객체 vs 불변 타입 객체

# 가변 타입: 한 번 생성한 인스턴스의 속성 변경 가능. 예: list
# 불변 타입: 한 번 생성한 인스턴스의 속성 변경 불가. 예: tuple

# 주의사항: 클래스 메서드에서 클래스 변수를 호출할 때 앞에 클래스명을 따온다.
# e.g. class Clock:
#          min = 0
#          def time(self):
#              self.time = Clock.min