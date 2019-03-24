# 3.5 함수 인자 풀기

def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

print_vector(1, 0, 0)


tuple_vec = (1, 1, 0)
list_vec = [1, 1, 1]

print_vector(
    tuple_vec[0],
    tuple_vec[1],
    tuple_vec[2]
)

print_vector(
    list_vec[0],
    list_vec[1],
    list_vec[2]
)

print_vector(*tuple_vec)
print_vector(*list_vec)

genexpr = (x * x for x in range(3))
print_vector(*genexpr)

dict_vec = {'y': 0, 'z': 1, 'x': 1}
print_vector(**dict_vec) # 순서는 보장되지 않는다.
print_vector(*dict_vec)
