def add(x: float, y: float) -> float:

    """
    Adds x to y.

    Input
    -----
        x: a float
        y: a float

    Output
    ------
        A float   
    """

    return x + y

def divide(x: float, y: float) -> float:

    """
    Divides x by y.

    Input
    -----
        x: a float
        y: a float

    Output
    ------
        A float 
    """

    return x/y #don't need to modify, python already returns zerodivisionerror

def factorial(x: int) -> int:

    """
    Returns the faktorial of a number x.

    Input
    -----
        x: An integer

    Output
    ------
        An integer
    """

    if x < 0:
        raise ValueError
    elif isinstance(x, float):
        raise TypeError
    else:
        fac = 1
        for i in range(1, x+1):
            fac = fac*i
        return fac

def sin(x: float, N = 20) -> float:

    """
    Returns sin(x) of a number x. Has a keyword argument N that can be specified.

    Input
    -----
        x: A float
        N: An int, by default set to 20

    Output
    ------
        A float
    """

    val = 0
    for n in range(N):
        val += divide((-1)**n*x**(2*n+1), (factorial(2*n+1)))
    return val   

def sqrt(y: float, x0: float = 1, tol: float = 1e-12) -> float:

    """
    Returns square root of number y, given a number x0 < y, and a tolerance.

    Input
    -----
        y: A float
        x: A float, by default set to 1
        tol: A float, by default set to 1e-12
    
    Output
    ------
        A float
    """

    while True:
        if abs(x0**2 - y) <= tol:
            break
        x0 = (x0 + y / x0) / 2
    return x0
