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



# 객체 지향 프로그래밍의 4가지 기둥이란?? 

'''
추상화( Abstraction )
캡슐화(Encapsulation)
상속(Inheritance)
다형성(Polymorphism)

'''


'''
추상화란?

어떤 것을 사용할 때 몰라도 되는 부분은 감추고 꼭 알아야 하는 부분만 드러내는 것을 추상화라고 한다.

프로그래밍에서 추상화란 프로그래머들이 특정 코드를 사용할 때 필수적인 정보를 제외한 세부사항을 가리는 것이다.

변수명을 지정하는 것이나 함수, 클래스를 쓰는 것도 다 추상화이다.
추상화를 잘 하려면 이름을 잘 지어야 한다.

또 문서화(docstring) 하는 방법도 있다.
지금 쓰고 있는 것이 docstring이다.

이 docstring으로 변수나 함수, 클래스에 대한 설명을 추가로 하면 좋다.
help(class)를 하면 docstring 모음을 볼 수 있다.

파이썬은 동적 타입이라 변수의 타입을 정의하지 않는다.
type hinting으로 변수의 type을 혼동하는 단점을 보완할 수 있다.
변수 뒤에 colon을 쓰고 type을 쓰면 된다.

e.g. 

deposit: float = 200

def deposit(self, amount: float) -> None:    (return 값의 data type을 정해줄 수도 있다.)
type hinting을 지키지 않아도 에러는 나지 않는다. 하지면 에디터에서 경고 메시지는 뜬다.

'''

'''
캡슐화란?

1. 객체의 일부 구현 내용에 대한 외부로부터의 직접적인 액세스를 차단하는 것
2. 객체의 속성과 그것을 사용하는 행동을 하나로 묶는 것 (특정 메서드를 통해서만 어떤 변수에 접근할 수 있게 하는 것)


1번에 의하면 self.__age 형식으로 __를 붙이면 변수를 직접적으로 호출할 수 없다.
2번에 의하면 클래스 내부에 메서드를 만들어서 접근 불가능한 변수를 호출할 수 있다.

위의 메서드 중 접근 금지 변수의 값을 읽는 메서드를 getter 메서드, 설정하는 메서드를 setter 메서드라고 한다.  
메서드에 예외처리를 해주는 것도 중요하다. (예: 음수 age 값은 0으로 처리하기)

네임 맹글링이란?
dir(class)를 통해 클래스를 호출하면 클래스의 메서드들이 보이는데, _class__method 처럼 앞에 _class를 붙여서 메서드를 보여준다. 이를 네임 맹글링이라 한다.
해당 명칭으로 호출을 하면 접근 금지인 값도 볼 수 있다.

변수나 메서드에 _를 붙이면 함부로 접근하지 말라는 표시이다. 따라서, __ 대신 _를 쓰도록 한다.

파이썬은 왜 언어 자체에서 캡슐화를 지원하지 않는가?
-> 파이썬의 문화이다.

캡슐화를 안했는데 나중에 캡슐화를 하고 싶을 경우?
-> property라는 데코레이터 함수를 사용한다.

@property                                 -> getter 메서드
def age(self):
    print('나이를 리턴합니다')
    return self._age
@age.setter                               -> setter 메서드
def age(self, value):
    print('나이를 설정합니다.')
    if value < 0:
        print('나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.')
        self._age = 0
    else:
        self._age = value

위처럼 함수를 정의하면

young.age
혹은
young.age = 30 을 하면

위 데코레이터 함수인 age를 인식해서 getter, setter 메서드를 사용하게 된다.
'''

'''
상속이란?

두 클래스 사이에 부모-자식 관계를 설정하는 것

자식 클래스는 부모 클래스의 모든 변수와 메서드를 물려 받는다.

자식 클래스를 정의할 때 인자로 부모 클래스를 넣으면 된다.
e.g. class Benz(Car):
         ....

help(~) 쓰면 상속관계를 보여준다.

Method resolution order:
    Cashier                 자식
    Employee                부모
    builtins.object         모든 클래스는 자동으로 이것을 부모로 둔다.

class.mro() 로 따로 확인할 수도 있다.

isinstance(instance, class) -> 특정 인스턴스가 해당 클래스의 인스턴스인지 불린을 반환
참고: 자식 클래스의 인스턴스는 부모 클래스의 인스턴스이기도 하다.

issubclass(subclass, class) -> 특정 클래스가 다른 클래스의 자식 클래스인지 불린을 반환

부모 클래스에게 물려 받은 것을 자식 클래스가 변형하여 사용하는 것을 오버라이딩이라고 한다.
오버라이딩 하는 법:

1. 같은 이름의 메서드를 다시 정의한다.
2. Class.__method__(self, a, b) 를 써서 기존 메서드를 호출하고 밑에 새로운 줄을 추가한다.
3. super().__method__(a, b) 를 사용한다.

오버라이딩이 가능한 이유는 mro에 나와있는 클래스 순서대로 메서드를 탐색하기 때문이다.

다중상속도 가능하다. 부모 클래스 여러 개를 선언하면 된다.
단점: 위의 3번처럼 super()을 쓰면 부모 클래스가 어떤 건지 모르기 때문에 2번을 써야만 한다.
'''