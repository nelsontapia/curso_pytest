# fist test
# run in console: python -m pytest
import pytest

def test_one_plus_one():
   assert 1 + 1 == 2

def test_one_plus_two():
    a = 1
    b = 2
    c = 3

    assert a + b == c

def test_one_plus_third():
    with pytest.raises(ZeroDivisionError) as e:
        num  = 1 / 0

    assert 'division by zero' in str(e.value)


# Multiplication test ideas

# two positive integers
# identity: multiplying any number by 1
# zero: multiplying any number by 0
# positive by a negative
# negative by a negative
# multiply floats

# --------------
# A parametrized test funtion
# --------------

products = [
    (2,3,6),            # Positive
    (1,99,99),          # identity
    (0, 99, 0),         # zero
    (3, -4, -12),       # positive by negative
    (-5, -5, 25),       # negative by negative
    (2.5, 6.7, 16.75)   # floats
]

@pytest.mark.parametrize('a, b, product',products)
def test_multiplication(a,b,product):
    assert a * b == product
    

list_arg = [
    (1,1,2),
    (4,5,9),
    (2,2,4)
]

@pytest.mark.parametrize('ent_1,ent_2,prod',list_arg)
def test_param_entries(ent_1,ent_2,prod):
    assert ent_1 + ent_2 == prod 