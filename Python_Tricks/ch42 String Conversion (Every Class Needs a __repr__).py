# 4.2 문자열 변환(모든 클래스는 __repr__이 필요하다)

import datetime


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


my_car = Car('red', 37281)

print(my_car)
# <__main__.Car object at 0x000001C7415908D0>

# >>> my_car
# <__console__.Car object at 0x109b73da0>


class Car1:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'

# __str__를 구현하면 to_string()시 사용됨.


my_car1 = Car1('red', 37281)

print(my_car1)
# a red car

# 콘솔에서는 여전히 id를 포함한 내용 출력
# >>> my_car1
# <__console__.Car object at 0x109ca24e0>


class Car2:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return '__str__ for Car'

    def __repr__(self):
        return '__repr__ for Car'


my_car2 = Car2('red', 37281)

print(my_car2)
# __str__ for Car

# >>> my_car
# __repr__ for Car

print(str([my_car2]))
# [__repr__ for Car]

print(repr(my_car2))
# __repr__ for Car

# __str__ 읽을 수 있어야 한다는 정도
# __repr__ 명확해야 한다.
# 무슨 말이야!!!!!

# import datetime
today = datetime.date.today()
print(str(today))
# 2019-02-06

print(repr(today))
# datetime.date(2019, 2, 6)

# __repr__이 반환한 문자열을 복사하여 붙여 넣어서
# 파이선 코드로 실행하여 원래 객체를 만들수 있어야 함
# 하지만 이것은 실천하기 어렵고, 보통 다들 기대하지 않음


# __str__를 추가하지 않으면 __repr__를 사용함


class Car_repr:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'


print(str(Car_repr('red', 37281)))
# __repr__ for Car


# 포맷 문자열 문법
# https://docs.python.org/ko/3.7/library/string.html#format-string-syntax

# conversion 필드는 세 가지 변환 플래그가 지원됩니다:
# '!s' 는 값에 str() 을 호출하고,
# '!r' 은 값에 repr() 을 호출하고,
# '!a' 는 값에 ascii() 를 호출합니다.


class Car_repr2:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f'{self.__class__.__name__}({self.color!r}, {self.mileage!r})'


print(repr(Car_repr2('red', 37281)))
# Car_repr2('red', 37281)

print(repr(Car_repr2('red', 37281)))
# Car_repr2('red', 37281)
