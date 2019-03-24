# 4.3 자신만의 예외 클래스 정의하기
#     Defining Your Own Exception Classes


def validate(name):
    if len(name) < 10:
        raise ValueError


# validate('joe')
# Traceback (most recent call last):
#   File "D:\GitHub\books\Python_Tricks\ch43.py", line 10, in <module>
#     validate('joe')
#   File "D:\GitHub\books\Python_Tricks\ch43.py", line 7, in validate
#     raise ValueError
# ValueError

class NameTooShortError(ValueError):
    pass


def validate2(name):
    if len(name) < 10:
        raise NameTooShortError(name)


# validate2('jane')
# Traceback (most recent call last):
#   File "D:\GitHub\books\Python_Tricks\ch43.py", line 27, in <module>
#     validate2('jane')
#   File "D:\GitHub\books\Python_Tricks\ch43.py", line 24, in validate2
#     raise NameTooShortError(name)
# __main__.NameTooShortError: jane


# EAFP
# 허락보다는 용서를 구하기가 쉽다 (Easier to ask for forgiveness than permission).
# 이 흔히 볼 수 있는 파이썬 코딩 스타일은, 올바른 키나 어트리뷰트의 존재를 가정하고,
# 그 가정이 틀리면 예외를 잡습니다.
# 이 깔끔하고 빠른 스타일은 많은 try 와 except 문의 존재로 특징지어집니다.
# 이 테크닉은 C와 같은 다른 많은 언어에서 자주 사용되는 LBYL 스타일과 대비됩니다.

# LBYL
# 뛰기 전에 보라 (Look before you leap).
# 이 코딩 스타일은 호출이나 조회를 하기 전에 명시적으로 사전 조건들을 검사합니다.
# 이 스타일은 EAFP 접근법과 대비되고, 많은 if 문의 존재로 특징지어집니다.
# 다중 스레드 환경에서, LBYL 접근법은 "보기"와 "뛰기" 간에 경쟁 조건을 만들게 될 위험이 있습니다.
# 예를 들어, 코드 if key in mapping: return mapping[key] 는 검사 후에, 하지만 조회 전에,
# 다른 스레드가 key 를 mapping 에서 제거하면 실패할 수 있습니다.
# 이런 이슈는 록이나 EAFP 접근법을 사용함으로써 해결될 수 있습니다.

# https://docs.python.org/ko/3/glossary.html
