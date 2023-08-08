from calculator import add, divide, factorial, sin, sqrt
import math as m
import pytest

@pytest.mark.parametrize("arg1, arg2, output", [(1,2,3), (0,6,6), (-1,-5,-6)])
def test_add(arg1, arg2, output):
    assert add(arg1,arg2) == output or m.isclose(add(arg1,arg2), output)
    
@pytest.mark.parametrize("arg1, arg2, output", [(5,2,2.5), (1,3,1/3), (6,2,3), (4,0,ZeroDivisionError)])
def test_divide(arg1, arg2, output):
    if type(output) == type and issubclass(output, Exception):
        with pytest.raises(output):
            divide(arg1,arg2)   
    else:
        assert divide(arg1, arg2) == output

@pytest.mark.parametrize("arg, output", [(1,1), (2,2), (3,6), (5,120), (0,1), (-1, ValueError), (1/3, TypeError)])
def test_factorial(arg, output):
    if type(output) == type and issubclass(output, Exception):
        with pytest.raises(output):
            factorial(arg)   
    else:
        assert factorial(arg) == output
    
@pytest.mark.parametrize("arg, output", [(0,0), (m.pi/4,1/m.sqrt(2)), (m.pi/2, 1), (3*m.pi/2,-1)])
def test_sin(arg, output):
    assert sin(arg) == output or m.isclose(sin(arg), output)

@pytest.mark.parametrize("arg, output", [(2,m.sqrt(2)), (3,m.sqrt(3)), (25,5), (16,4)])
def test_sqrt(arg, output):
    assert  sqrt(arg) == output or m.isclose(sqrt(arg), output)