"""
# 4.1 객체 비교: 'is' 대 '=='
"""

A = [1, 2, 3]
B = A

print(A)

print(B)

print(A == B)

print(A is B)

C = list(A)

print(C)

print(A == C)

print(A is C)
