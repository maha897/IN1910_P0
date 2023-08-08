from typing import Callable
import numpy as np

def left_riemann_sum(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    x = np.linspace(1,10, 100)
    for i in range(n):
        fxdx = (x[i+1] - x[i])*f(x[i])

f = lambda x: (3*x**2)*np.exp(x**3)
left_riemann_sum(f, 0, 1, 100)

def midpoint(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    for i in range(n):
        fxdx = ((x[i+1]-x[i])/2)*(f(x[i]+f[i+1]))