
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


shoes = {'name': 'Fancy Shoes', 'price': 14900}


apply_discount(shoes, 0.25)

# 11175

apply_discount(shoes, 2.0)

# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     apply_discount(shoes, 2.0)
#   File "<pyshell#5>", line 3, in apply_discount
#     assert 0 <= price <= product['price']
# AssertionError
